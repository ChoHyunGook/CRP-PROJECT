# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         docbuild/writers.py
# Purpose:      music21 documentation writer to rst
#
# Authors:      Josiah Wolf Oberholtzer
#               Christopher Ariza
#               Michael Scott Cuthbert
#
# Copyright:    Copyright © 2013-15 Michael Scott Cuthbert and the music21 Project
# License:      BSD, see license.txt
# ------------------------------------------------------------------------------
import logging
import os
import pathlib
import re
import shutil

from more_itertools import windowed

from music21 import common
from music21 import exceptions21
from music21 import environment

from . import documenters
from . import iterators

environLocal = environment.Environment('docbuild.writers')

class DocumentationWritersException(exceptions21.Music21Exception):
    pass


class _BuildDirectoryFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        if not msg.startswith('Making directory'):
            return True
        dirMade = msg[len('Making directory '):].strip()
        if not os.path.exists(dirMade):
            return True
        return False

class DocumentationWriter:
    '''
    Abstract base class for writers.

    Call .run() on the object to make it work.
    '''
    def __init__(self):
        self.outputDirectory = None
        self.docBasePath = common.getRootFilePath() / 'documentation'
        self.docSourcePath = self.docBasePath / 'source'
        self.docGeneratedPath = self.docBasePath / 'autogenerated'

    def run(self):
        raise NotImplementedError

    # PUBLIC METHODS #
    def sourceToAutogenerated(self, sourcePath):
        '''
        converts a sourcePath to an outputPath

        generally speaking, substitutes "source" for "autogenerated"
        '''
        outputPath = str(sourcePath.resolve()).replace(
            str(self.docSourcePath), str(self.docGeneratedPath))
        return pathlib.Path(outputPath)


    def setupOutputDirectory(self, outputDirectory=None):
        '''
        creates outputDirectory (a pathlib.Path) if it does not exist.

        Looks at self.outputDirectory if not there.
        '''
        if outputDirectory is None:
            outputDirectory = self.outputDirectory
            if outputDirectory is None:
                raise DocumentationWritersException(
                    'Cannot setup output directory without guidance'
                )
        if outputDirectory.exists():
            return

        outputDirectory.mkdir()

class StaticFileCopier(DocumentationWriter):
    '''
    Copies static files into the autogenerated directory.
    '''
    def run(self):
        excludedFiles = ['.ipynb', '__pycache__', '.pyc', '.gitignore', 'conf.py', '.DS_Store']
        for subPath in sorted(self.docSourcePath.rglob('*')):
            if subPath.is_dir():
                self.setupOutputDirectory(self.sourceToAutogenerated(subPath))
                continue

            runIt = True
            for ex in excludedFiles:
                if subPath.name.endswith(ex):
                    runIt = False
            if runIt is False:
                continue

            outputFilePath = self.sourceToAutogenerated(subPath)
            if (outputFilePath.exists()
                    and outputFilePath.stat().st_mtime > subPath.stat().st_mtime):
                print(f'\tSKIPPED {common.relativepath(outputFilePath)}')
            else:
                shutil.copyfile(str(subPath), str(outputFilePath))
                print(f'\tWROTE   {common.relativepath(outputFilePath)}')



class ReSTWriter(DocumentationWriter):
    '''
    Abstract base class for all ReST writers.
    '''
    def run(self):
        raise NotImplementedError

    def write(self, filePath, rst):
        '''
        Write ``rst`` (a unicode string) to ``filePath``, a pathlib.Path()
        only overwriting an existing file if the content differs.
        '''
        shouldWrite = True
        if filePath.exists():
            oldRst = common.readFileEncodingSafe(filePath, firstGuess='utf-8')
            if rst == oldRst:
                shouldWrite = False
            else:
                pass
                # # uncomment for  help in figuring out why a file keeps being different...
                # import difflib
                # print(common.relativepath(filePath))
                # print('\n'.join(difflib.ndiff(rst.split('\n'), oldRst.split('\n'))))

        if shouldWrite:
            with filePath.open('w', encoding='utf-8') as f:
                try:
                    f.write(rst)
                except UnicodeEncodeError as uee:
                    raise DocumentationWritersException(
                        f'Could not write {filePath} with rst:\n{rst}'
                    ) from uee
            print(f'\tWROTE   {common.relativepath(filePath)}')
        else:
            print(f'\tSKIPPED {common.relativepath(filePath)}')

class ModuleReferenceReSTWriter(ReSTWriter):
    '''
    Writes module reference ReST files, and their index.rst file.
    '''
    def __init__(self):
        super().__init__()
        self.outputDirectory = self.docGeneratedPath / 'moduleReference'
        self.setupOutputDirectory()

    def run(self):
        moduleReferenceDirectoryPath = self.outputDirectory
        referenceNames = []
        for module in list(iterators.ModuleIterator()):
            moduleDocumenter = documenters.ModuleDocumenter(module)
            if (not moduleDocumenter.classDocumenters
                    and not moduleDocumenter.functionDocumenters):
                continue
            rst = '\n'.join(moduleDocumenter.run())
            referenceName = moduleDocumenter.referenceName
            referenceNames.append(referenceName)
            fileName = f'{referenceName}.rst'
            rstFilePath = moduleReferenceDirectoryPath / fileName

            try:
                self.write(rstFilePath, rst)
            except TypeError as te:  # pragma: no cover
                raise TypeError(f'File failed: {rstFilePath}, reason: {te}')

        self.writeIndexRst(referenceNames)

    def writeIndexRst(self, referenceNames):
        '''
        Write the index.rst file from the list of reference names
        '''
        lines = []
        lines.append('.. moduleReference:')
        lines.append('')
        lines.append('.. WARNING: DO NOT EDIT THIS FILE:')
        lines.append('   AUTOMATICALLY GENERATED.')
        lines.append('')
        lines.append('**Module Reference**')
        lines.append('=========================')
        lines.append('')
        lines.append('.. toctree::')
        lines.append('   :maxdepth: 1')
        lines.append('')
        for referenceName in sorted(referenceNames):
            lines.append(f'   {referenceName}')
        rst = '\n'.join(lines)
        indexFilePath = self.outputDirectory / 'index.rst'
        self.write(indexFilePath, rst)



class CorpusReferenceReSTWriter(ReSTWriter):
    '''
    Write the corpus reference ReST file: referenceCorpus.rst
    into about/
    '''
    def __init__(self):
        super().__init__()
        self.outputDirectory = self.docGeneratedPath / 'about'
        self.setupOutputDirectory()


    def run(self):
        corpusReferenceFilePath = self.outputDirectory / 'referenceCorpus.rst'
        lines = documenters.CorpusDocumenter().run()
        rst = '\n'.join(lines)
        self.write(corpusReferenceFilePath, rst)


class IPythonNotebookReSTWriter(ReSTWriter):
    '''
    Converts IPython notebooks into ReST, and handles their associated image
    files.

    This class wraps the 3rd-party ``nbconvert`` Python script.
    '''
    def __init__(self):
        from .iterators import IPythonNotebookIterator
        super().__init__()
        self.ipythonNotebookFilePaths = list(IPythonNotebookIterator())
        # Do not run self.setupOutputDirectory()

    def run(self):
        for ipythonNotebookFilePath in self.ipythonNotebookFilePaths:
            nbConvertReturnCode = self.convertOneNotebook(ipythonNotebookFilePath)
            if nbConvertReturnCode is True:
                self.cleanupNotebookAssets(ipythonNotebookFilePath)
                print(f'\tWROTE   {common.relativepath(ipythonNotebookFilePath)}')
            else:
                print(f'\tSKIPPED {common.relativepath(ipythonNotebookFilePath)}')

                # do not print anything for skipped -checkpoint files
        self.writeIndexRst()

    def writeIndexRst(self):
        '''
        Writes out the index.rst file for the usersGuide directory.

        Does not do any other index.rst files. Just from the links in the
        user's guide.  I added this because keeping up the visual
        table of contents and the index.rst was making my life miserable.

        >>> ipRestWriter = IPythonNotebookReSTWriter()
        >>> #_DOCS_HIDE ipRestWriter.writeIndexRst()

        WROTE   autogenerated/usersGuide/index.rst
        '''
        tocFile = 'usersGuide_99_Table_of_Contents'
        ipFilePaths = [x for x in self.ipythonNotebookFilePaths if 'usersGuide' in x.name]
        if not ipFilePaths:
            raise DocumentationWritersException(
                'No iPythonNotebook files were converted; '
                + 'you probably have a problem with pandoc or nbconvert not being installed.'
            )
        usersGuideDir = self.notebookFilePathToRstFilePath(ipFilePaths[0]).parent
        tocFp = usersGuideDir / (tocFile + '.rst')
        # '/Users/cuthbert/git/music21base/music21/documentation/autogenerated/usersGuide'
        usersGuideInOrder = [tocFile]

        with tocFp.open('r', encoding='utf-8') as tocFileHandler:
            for line in tocFileHandler:
                matched = re.search(r'<(usersGuide.*)>', line)
                if matched:
                    usersGuideInOrder.append(matched.group(1))


        lines = []
        lines.append('.. usersGuide:')
        lines.append('')
        lines.append('.. WARNING: DO NOT EDIT THIS FILE:')
        lines.append('   AUTOMATICALLY GENERATED.')
        lines.append('')
        lines.append("User's Guide")
        lines.append('================')
        lines.append('')
        lines.append('.. toctree::')
        lines.append('   :maxdepth: 1')
        lines.append('')
        for referenceName in usersGuideInOrder:
            lines.append(f'   {referenceName}')

        rst = '\n'.join(lines)
        indexFilePath = usersGuideDir / 'index.rst'
        self.write(indexFilePath, rst)


    def cleanupNotebookAssets(self, ipythonNotebookFilePath):
        '''
        Deletes all .text files in the directory of ipythonNotebookFilePath
        (a pathlib.Path).
        '''
        notebookFileNameWithoutExtension = ipythonNotebookFilePath.stem
        notebookParentDirectoryPath = ipythonNotebookFilePath.parent
        imageFileDirectoryPath = notebookParentDirectoryPath / notebookFileNameWithoutExtension
        imageFileDirectoryPath = self.sourceToAutogenerated(imageFileDirectoryPath)
        if not imageFileDirectoryPath.exists():
            return
        for filePath in sorted(imageFileDirectoryPath.glob('*.text')):
            filePath.unlink()

    @property
    def rstEditingWarningFormat(self):
        result = []
        result.append('.. WARNING: DO NOT EDIT THIS FILE:')
        result.append('   AUTOMATICALLY GENERATED.')
        result.append('   PLEASE EDIT THE .py FILE DIRECTLY.')
        result.append('')
        return result


    def notebookFilePathToRstFilePath(self, ipythonNotebookFilePath):
        if not ipythonNotebookFilePath.exists():
            raise DocumentationWritersException(
                f'No iPythonNotebook with filePath {ipythonNotebookFilePath}')
        notebookFileNameWithoutExtension = ipythonNotebookFilePath.stem
        notebookParentDirectoryPath = ipythonNotebookFilePath.parent
        rstFileName = notebookFileNameWithoutExtension + '.rst'
        rstFilePath = self.sourceToAutogenerated(notebookParentDirectoryPath / rstFileName)
        return rstFilePath

    def convertOneNotebook(self, ipythonNotebookFilePath):
        '''
        converts one .ipynb file to .rst using nbconvert.

        returns True if IPythonNotebook was converted.
        returns False if IPythonNotebook's converted .rst file is newer than the .ipynb file.

        sends AssertionError if ipythonNotebookFilePath does not exist.
        '''
        rstFilePath = self.notebookFilePathToRstFilePath(ipythonNotebookFilePath)
        if rstFilePath.exists():
            # print(rstFilePath + ' exists')
            # rst file is newer than .ipynb file, do not convert.

            if rstFilePath.stat().st_mtime > ipythonNotebookFilePath.stat().st_mtime:
                return False

        self.runNBConvert(ipythonNotebookFilePath)
        # uses this convoluted way of reading because 'encoding' was an invalid keyword argument
        # for the built-in 'open' in old python, and never upgraded.
        with rstFilePath.open('r', encoding='utf8') as f:
            oldLines = f.read().splitlines()

        lines = self.cleanConvertedNotebook(oldLines, ipythonNotebookFilePath)
        with rstFilePath.open('w', encoding='utf8') as f:
            f.write('\n'.join(lines))

        return True


    def cleanConvertedNotebook(self, oldLines, ipythonNotebookFilePath):
        '''
        Take a notebook directly as parsed and make it look better for HTML

        Fixes up the internal references to class, ref, func, meth, attr.
        '''
        notebookFileNameWithoutExtension = ipythonNotebookFilePath.stem
        # imageFileDirectoryName = self.sourceToAutogenerated(notebookFileNameWithoutExtension)

        ipythonPromptPattern = re.compile(r'^In\[[\d ]+]:')
        mangledInternalReference = re.compile(
            r':(class|ref|func|meth|attr):``?(.*?)``?')
        newLines = [f'.. _{notebookFileNameWithoutExtension}:',
                    '']
        newLines += self.rstEditingWarningFormat
        currentLineNumber = 0

        while currentLineNumber < len(oldLines):
            currentLine = oldLines[currentLineNumber]
            # Remove all IPython prompts and the blank line that follows:
            if ipythonPromptPattern.match(currentLine) is not None:
                currentLineNumber += 2
                continue
            # Correct the image path in each ReST image directive:
            elif currentLine.startswith('.. image:: '):
                imageFileName = currentLine.partition('.. image:: ')[2]
                imageFileShort = imageFileName.split(os.path.sep)[-1]
                if notebookFileNameWithoutExtension in currentLine:
                    newImageDirective = f'.. image:: {imageFileShort}'
                    newLines.append(newImageDirective)
                else:
                    newLines.append(currentLine)
                currentLineNumber += 1
            elif '# ignore this' in currentLine:
                if '.. code:: ' in newLines[-2]:
                    # print('STOP HERE!')
                    newLines.pop()  # remove blank line
                    newLines.pop()  # remove '.. code:: python'

                # compensate for:
                # -- # ignore this
                # -- %load_ext music21.ipython21.ipExtension
                # by skipping two lines.
                currentLineNumber += 2
                # TODO: Skip all % lines, without looking for '#ignore this'
            # Otherwise, nothing special to do, just add the line to our results:
            else:
                # fix cases of inline :class:`~music21.stream.Stream` being
                # converted by markdown to :class:``~music21.stream.Stream``
                newCurrentLine = mangledInternalReference.sub(
                    r':\1:`\2`',
                    currentLine
                )
                newLines.append(newCurrentLine)
                currentLineNumber += 1

        lines = self.blankLineAfterLiteral(newLines)

        return lines

    def blankLineAfterLiteral(self, oldLines):
        '''
        Guarantee a blank line after literal blocks.
        '''
        lines = [oldLines[0]]  # start with first line.
        for first, second in windowed(oldLines, 2):
            if (first.strip()
                    and first[0].isspace()
                    and second.strip()
                    and not second[0].isspace()):
                lines.append('')
            lines.append(second)
            if '.. parsed-literal::' in second:
                lines.append('   :class: ipython-result')
        return lines

    def runNBConvert(self, ipythonNotebookFilePath):
        try:
            # noinspection PyPackageRequirements
            from nbconvert import nbconvertapp as nb
        except ImportError:
            environLocal.warn('nbconvert is not installed, run pip3 install nbconvert')
            raise

        outputPath = os.path.splitext(
            str(self.sourceToAutogenerated(ipythonNotebookFilePath))
        )[0]

        app = nb.NbConvertApp.instance()
        app.initialize(argv=['--to', 'rst', '--output', outputPath,
                             str(ipythonNotebookFilePath)])
        app.writer.build_directory = str(ipythonNotebookFilePath.parent)
        app.writer.log.addFilter(_BuildDirectoryFilter())
        app.start()
        return True


if __name__ == '__main__':
    i = IPythonNotebookReSTWriter()
    p5 = i.ipythonNotebookFilePaths[5]
    i.convertOneNotebook(p5)
    import music21
    music21.mainTest('moduleRelative')
