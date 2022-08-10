export class FileService {
  static getFileExtension(fileName: string): string {
    const fileNames: Array<string> = fileName.split(".");

    if (fileNames.length === 0) {
      return "";
    }

    console.log(" ############## ");
    console.log(" fileNames : " + fileNames);
    console.log(" ############## ");

    return fileNames[fileNames.length - 1];
  }

  public getFormData(file: File): FormData {
    const formData = new FormData();
    formData.append("file " , file);
    return formData;
  }
}
