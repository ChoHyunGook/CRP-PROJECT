import numpy as np
import pandas as pd
from icecream import ic

from hello import Quiz20
from hello.domains import myRandom, my803
from context.models import Model
import random
import string

class Quiz30:
    '''
            데이터프레임 문제 Q02
        ic| df:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
        '''

    def quiz30_df_4_by_3(self) -> None:

        columns = Quiz20.askicode(65,68)
        d1 = [i for i in range(1, 13)]
        d2=[d1[i:i + 3] for i in range(0, len(d1), 3)]

        df = pd.DataFrame(d2, index=range(1, 5), columns=columns)
        # 위 식을 리스트결합 형태로 분해해서 조립하시오

        ic(df)
        return None
#http://pertinency.blogspot.com/2019/10/blog-post_7.html
    '''
            데이터프레임 문제 Q03.
            두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
            ic| df:     0   1   2
                    0  97  57  52
                    1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> str:
        data=Quiz30.random_cutter(10,100,6,3)
        df = pd.DataFrame(data, index=range(0, 2), columns=range(0,3))
        df1 = pd.DataFrame(np.random.randint(10,100,size=(2,3)))

        ic(df)
        ic(df1)
        return None

    '''
                데이터프레임 문제 Q04.
                국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                  ic| df4:        국어  영어  수학  사회
                            lDZid  57  90  55  24
                            Rnvtg  12  66  43  11
                            ljfJt  80  33  89  10
                            ZJaje  31  28  37  34
                            OnhcI  15  28  89  19
                            claDN  69  41  66  74
                            LYawb  65  16  13  20
                            QDBCw  44  32   8  29
                            PZOTP  94  78  79  96
                            GOJKU  62  17  75  49
        '''

    @staticmethod
    def id(chr_size) -> str:
        return ''.join([str(random.choice(string.ascii_uppercase)) for j in range(chr_size)])



    def quiz32_df_grade(self) -> str:
        data=Quiz30.random_cutter(0,101,40,4)
        col=['국어','영어','수학','사회']
        idx = [self.id(5) for i in range(10)]
        df1=pd.DataFrame(data,index=idx,columns=col)
        ic(df1)
        print('*' * 100)
        data1=np.random.randint(0,100,(10,4))
        idx1= [self.id(5) for i in range(10)]
        data2={i:j for i,j in zip(idx1,data1)}
        col2=['국어','영어','수학','사회']
        df2=pd.DataFrame.from_dict(data2,orient='index',columns=col2)
        ic(df2)
        print('*'*100)
        df3 = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), index=idx, columns=col)
        ic(df3)
        print('*'*100)
        dt=np.random.randint(0,100,(12,5))
        col3=['국','영','수','사','과']
        idx1=[self.id(5) for i in range(12)]
        df4=pd.DataFrame(dt,index=idx1,columns=col3)
        ic(df4)
        print('*'*100)
        dt1=np.random.randint(0,100,(12,5))
        data5={i:j for i,j in zip(idx1,dt1)}
        col4 = ['국', '영', '수', '사', '과']
        df5=pd.DataFrame.from_dict(data5,orient='index',columns=col4)
        ic(df5)
        print('*'*100)
        df6=pd.DataFrame(np.random.randint(0,100,(12,5)),index=idx1,columns=col3)
        ic(df6)



        '''ls=[]
        for i in range(10):
            name=""
            for j in range(5):
                name += (str(random.choice(string.ascii_uppercase)))
            ls.append(name)'''




        return None

    def quiz33_df_loc(self) -> str:
        #temp=self.create_df(keys=['a','b','c','d'],vals=np.random.randint(1,4000,4),len=3)
        #ic(temp)
        #print('*'*100)

        df=pd.DataFrame(np.random.randint(0,100,(24,4)),index=my803(),columns=['자바','파이썬','자바스크립트','SQL'])
        #ic(df)
        model = Model()
        #model.save_model('grade_backup.csv', dframe=df)

        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        grade_df=model.new_model('grade_backup.csv')
        #ic(grade_df)

        print('Q1. 파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:,'파이썬']
        ic(python_scores)

        print('Q2. 조현국의 점수만 출력하시오.')
        cho_scores=grade_df.loc['조현국']
        ic(type(cho_scores))
        ic(cho_scores)
        cho_scores_do=grade_df.loc[['조현국']]
        ic(type(cho_scores_do))
        ic(cho_scores_do)




        return None







    def quiz34_iloc(self) -> str:
        # ic(temp.iloc[0])
        '''ic| temp.iloc[0]: a    2169
                             b    2622
                             c     613
                             d    1029
                              Name: 0, dtype: int32'''
        # ic(temp.iloc[[0]])
        '''ic| temp.iloc[[0]]:       a     b    c     d
                                0  3848  1200  293  1978'''
        # ic(temp.iloc[[0,1]])
        '''ic| temp.iloc[[0,1]]:       a     b    c     d
                                    0  1705  1280  685  1849
                                    1  1705  1280  685  1849'''
        # ic(temp.iloc[:3])
        '''ic| temp.iloc[:3]:       a     b     c     d
                                0  3504  1418  2058  3036
                                1  3504  1418  2058  3036
                                2  3504  1418  2058  3036'''
        # ic(temp.iloc[[True,False,True]])
        '''ic| temp.iloc[[True,False,True]]:       a     b     c     d
                                               0  2068  3461  1341  1951
                                               2  2068  3461  1341  1951'''
        # ic(temp.iloc[lambda x: x.index % 2 == 0])#내부함수
        '''ic| temp.iloc[lambda x: x.index % 2 == 0]:       a     b     c    d
                                                        0  1403  1226  3292  964
                                                        2  1403  1226  3292  964'''
        # ic(temp.iloc[0,1])
        '''ic| temp.iloc[0,1]: 3275'''
        # ic(temp.iloc[[0,2],[1,3]])
        '''ic| temp.iloc[[0,2],[1,3]]:       b     d
                                        0  1281  1600
                                        2  1281  1600'''
        # ic(temp.iloc[1:3,0:3])
        '''ic| temp.iloc[1:3,0:3]:       a     b     c
                                    1  1373  2847  3025
                                    2  1373  2847  3025'''

        # ic(temp.iloc[:, [True, False, True, False]])
        '''ic| temp.iloc[:, [True, False, True, False]]:      a     c
                                                         0  945  2251
                                                         1  945  2251
                                                         2  945  2251'''
        # ic(temp.iloc[:, lambda df: [0, 2]])
        '''ic| temp.iloc[:, lambda df: [0, 2]]:       a     c
                                                 0  1464  1866
                                                 1  1464  1866
                                                 2  1464  1866'''

        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None



    @staticmethod
    def random_cutter(start,end,point,cutter):
        d = [myRandom(start,end) for i in range(point)]
        d1 = [d[i:i + cutter] for i in range(0, len(d), cutter)]
        return d1

    @staticmethod
    def create_df(keys,vals,len):
        return pd.DataFrame([dict(zip(keys,vals)) for i in range(len)])