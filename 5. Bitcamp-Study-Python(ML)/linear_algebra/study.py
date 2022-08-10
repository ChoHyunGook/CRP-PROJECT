import numpy as np
import matplotlib.pyplot as plt

class Study(object):

    def __init__(self):
        self.W = np.random.rand(1, 1)
        self.b = np.random.rand(1)
        self.x_data = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 18, 20, 25, 28, 30]).reshape(-1, 1)
        self.t_data = np.array([5, 7, 20, 31, 40, 44, 46, 49, 60, 62, 70, 80, 85, 91, 92, 97, 98]).reshape(-1, 1)

    def loss_func(self, x, t):
        y = np.dot(x, self.W) + self.b
        return np.mean(np.power((t - y), 2))

    @staticmethod
    def numerical_derivative(f, x):
            # f : 미분하려고 하는 다변수 함수
            # x : 모든 변수를 포함하고 있는 ndarray
            delta_x = 1e-4
            # 미분한 결과를 저장할 ndarray
            derivative_x = np.zeros_like(x)

            # iterator를 이용해서 입력된변수 x들 각각에 대해 편미분 수행
            it = np.nditer(x, flags=['multi_index'])

            while not it.finished:
                idx = it.multi_index  # iterator의 현재 index를 tuple 형태로 추출

                # 현재 칸의 값을 잠시 저장
                tmp = x[idx]

                x[idx] = tmp + delta_x
                fx_plus_delta = f(x)  # f(x + delta_x)

                x[idx] = tmp - delta_x
                fx_minus_delta = f(x)  # f(x - delta_x)

                # 중앙치분방식
                derivative_x[idx] = (fx_plus_delta - fx_minus_delta) / (2 * delta_x)

                # 데이터 원상 복구
                x[idx] = tmp

                it.iternext()

            return derivative_x

        # 5. prediction
        # 학습종료 후 임의의 데이터에 대한 예측값을 알아오는 함수
    def predict(self, x):
        return np.dot(x, self.W) + self.b  # Hypothesis, Linear Regression Model

    def study(self):
        learning_rate = 0.0001 #6
        x_data = self.x_data
        t_data = self.t_data
        f = lambda x: self.loss_func(x_data, t_data)
        # 7. 학습 진행
        # 반복해서 W와 b를 업데이트하며 학습 진행
        for step in range(90000):
            self.W = self.W - learning_rate * self.numerical_derivative(f, self.W)  # W의 편미분
            self.b = self.b - learning_rate * self.numerical_derivative(f, self.b)  # b의 편미분

            if step % 9000 == 0:
                print('W : {}, b : {}, loss : {}'.format(self.W, self.b, self.loss_func(x_data, t_data)))

        # 8. 학습종료 후 예측
        print(self.predict(19))  # [[77.86823633]]

        # 데이터의 분포를 scatter로 확인
        plt.scatter(x_data.ravel(), t_data.ravel())
        plt.plot(x_data.ravel(), np.dot(x_data, self.W) + self.b)  # 직선
        plt.show()

if __name__ == '__main__':
    Study().study()