import random
import numpy as np
import pypianoroll
import music21


class PreProcess:
    def preprocess(self, path_str, filename):
        data = []
        path = Path(path_str).glob('**/*')
        for name in path:
            try:
                multitrack = pypianoroll.read(name)
            except:
                continue
            multitrack.binarize()

            multitrack.set_resolution(beat_resolution)

            pianoroll = (multitrack.stack() > 0)

            pianoroll = pianoroll[:, :, lowest_pitch:lowest_pitch + n_pitches]

            n_total_measures = multitrack.get_max_length() // measure_resolution

            candidate = n_total_measures - n_measures
            target_n_samples = min(n_total_measures // n_measures, n_samples_per_song)

            for idx in np.random.choice(candidate, target_n_samples, False):
                start = idx * measure_resolution
                end = (idx + n_measures) * measure_resolution
                if (pianoroll.sum(axis=(1, 2)) < 10).any():
                    continue
                data.append(pianoroll[:, start:end])

        random.shuffle(data)
        data = np.stack(data)
        print(f"DATA shape : {data.shape}")
        np.savez_compressed(f'{filename}.npz', data=data)

    preprocess('midis', 'midis')
