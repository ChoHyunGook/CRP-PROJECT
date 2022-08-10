from pypianoroll import Multitrack
import os
from glob import glob

os.makedirs('result', exist_ok=True)

pianorolls = glob('exp/default/results/inference/pianorolls/*/*.npz')

for pianoroll_path in pianorolls:
    name, _ = os.path.splitext(os.path.basename(pianoroll_path))
    m = Multitrack(pianoroll_path)

    m.write('result/%s.mid' % name)
