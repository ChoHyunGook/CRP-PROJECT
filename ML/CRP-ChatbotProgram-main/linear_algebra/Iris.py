from sklearn.datasets import load_iris  # 사이킷런 패키지 임포트

class Iris:

    def __init__(self):
        self.iris = load_iris()


    def main(self):
        print(self.iris.data[0, :])


if __name__ == '__main__':
    Iris().main()
