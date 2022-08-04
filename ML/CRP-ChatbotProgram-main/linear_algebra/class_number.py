from sklearn.datasets import load_digits
from matplotlib import rc, font_manager, pyplot as plt
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())

class class_number:

    def __init__(self):
        self.digits = load_digits()
        self.samples = [0, 10, 20, 30, 1, 11, 21, 31]
        self.d=[]
        [self.d.append(self.digits.images[self.samples[i]]) for i in range(8)]


    def data_load(self):
        plt.figure(figsize=(8, 2))
        for i in range(8):
            plt.subplot(1, 8, i + 1)
            plt.imshow(self.d[i], interpolation='nearest', cmap=plt.cm.bone_r)
            plt.grid(False)
            plt.xticks([])
            plt.yticks([])
            plt.title("image {}".format(i + 1))
        plt.suptitle("숫자 0과 1 이미지")
        plt.tight_layout()
        #plt.show()
        plt.savefig('test_matrix.png',
                    facecolor='#eeeeee',
                    edgecolor='black',
                    format='png', dpi=200)

    def vector_image(self):
        v = [(self.d[i].reshape(64, 1)) for i in range(8)]
        plt.figure(figsize=(8, 3))
        for i in range(8):
            plt.subplot(1, 8, i + 1)
            plt.imshow(v[i], aspect=0.4,
                       interpolation='nearest', cmap=plt.cm.bone_r)
            plt.grid(False)
            plt.xticks([])
            plt.yticks([])
            plt.title("벡터 {}".format(i + 1))
        plt.suptitle("벡터화된 이미지", y=1.05)
        plt.tight_layout(w_pad=7)
        #plt.show()
        plt.savefig('test_vector.png',
                    facecolor='#eeeeee',
                    edgecolor='black',
                    format='png', dpi=200)



if __name__ == '__main__':
    class_number().data_load()
    class_number().vector_image()