import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir
import tensorflow.compat.v1 as tf
tf.executing_eagerly()
import numpy as np
import pandas as pd
from icecream import ic


class CabbageModel:
     def __init__(self) -> None:
          self.basedir = os.path.join(basedir, 'model')
          self.data = None
          self.x_data = None
          self.y_data = None
          
          
     
     #모델을 위한 전처리
     def preprocessing(self):
          self.data = pd.read_csv('C:/flask/model/data/price_data.csv')
          
          # avgTemp,minTemp,maxTemp,rainFall,avgPrice
          xy = np.array(self.data, dtype=np.float32)
          #np.array를 사용하면 dataframe을 슬라이싱 인덱싱이 가능한 ndarray로 변환이 가능하다. 
          #( Dataframe 과 ndarray 모두 2차원 매트릭스 구조를 가지고 있다.)
          ic(type(xy)) # <class 'numpy.ndarray'>
          ic(xy.ndim) # xy.ndim: 2  # 차원
          ic(xy.shape) # xy.shape: (2922, 6) # 행렬의 갯수
          self.x_data = xy[:, 1:-1]# 해당 날짜 기후요소 4개=> 슬라이싱 문법
          self.y_data = xy[:, [-1]]# 해당 날짜 배추가격 => 인덱싱 문법
     
        
     #모델생성
     def create_model(self):
          
          
          # 확률변수 데이터
          self.preprocessing()
          
          # 선형식제작 y= Wx+b
          #값 초기화 shape=>열
          X = tf.placeholder(tf.float32, shape=[None, 4])
          Y = tf.placeholder(tf.float32, shape=[None, 1])
          W = tf.Variable(tf.random_normal([4,1]), name ="weight")
          b = tf.Variable(tf.random_normal([1]), name="bias")
          hypothesis =tf.matmul(X, W)+ b #가설식 세우기,행열연산
          #=>matmul은 행렬곱 함수
          
          # 손실함수
          cost =  tf.reduce_mean(tf.square(hypothesis - Y))# 비용함수 설정 예측값 hypothesis에서 실제값 Y를 빼준다
          #=> reduce_mean 열단위로 평균을 내는 함수
          #=> square 제곱 함수
          
          # 최적화(Optimizer)-알고리즘
          #최적화 함수 설정 (학습률: 0.000005) 학습률은 데이터 정제의 정도이나, 유형에 따라 다르게 설정
          optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)#경사하강법(.train.GradientDescentOptimizer)
          train = optimizer.minimize(cost)#
          
          # 세션생성
          #세션값 만들어서 세션에 따라 학습수행
          sess = tf.Session()
          sess.run(tf.global_variables_initializer())
          
          # 트레이닝
          # 500번의 단계마다 진행 상황 확인하는 과정
          for step in range(100001):
               cost_, hypo_, _ = sess.run([cost,hypothesis,train], feed_dict={X: self.x_data, Y: self.y_data})
               if step % 500 == 0:
                    print("# %d 손실비용: %d" %(step, cost_))
                    print("-배추가격: %d" %(hypo_[0]))
          
          #모델 저장          
          saver = tf.train.Saver()
          saver.save(sess, os.path.join(self.basedir,'cabbage', 'cabbage.ckpt'),global_step=1000)
          print("학습된 모델을 저장했습니다.")
     
     #모델 로드
     def load_model(self, avg_temp, min_temp, max_temp, rain_fall):
          tf.disable_v2_behavior()
          # 선형식(가설)제작 y = Wx+b
          X = tf.placeholder(tf.float32, shape=[None, 4])
          W = tf.Variable(tf.random_normal([4,1]), name ="weight")
          b = tf.Variable(tf.random_normal([1]), name="bias")
          saver = tf.train.Saver()
          with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver.restore(sess, os.path.join(self.basedir, 'cabbage', 'cabbage.ckpt-1000'))
            data = [[avg_temp,min_temp,max_temp, rain_fall]]
            arr =np.array(data, dtype=np.float32)
            dict = sess.run(tf.matmul(X,W)+b,{X:arr[0:4]})
            print(dict)
          return int(dict[0])
     
if __name__ == '__main__':
     s=CabbageModel()
     s.create_model()