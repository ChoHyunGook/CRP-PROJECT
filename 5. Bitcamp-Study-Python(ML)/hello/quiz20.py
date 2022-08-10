import random
import urllib.request
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

from hello import Quiz00
from hello.domains import myRandom, my803
from icecream import ic

class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('-----------legacy------------')
        a =[]
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------comprehension------------')
        a2=[i for i in range(5)]
        print(a2)
        return None

    @staticmethod
    def quiz24zip() -> {}:
        soup = BeautifulSoup(urlopen('https://music.bugs.co.kr/chart/track/realtime/total'), 'lxml')
        cls_names=['artist', 'title']
        # print(''.join(i for i in Quiz20.soup_(soup, 'p', 'class', [i for i in cls_names])))
        a=[i for i in cls_names]
        ls1 = Quiz20.soup_(soup, 'p', 'class', 'title')
        ls2 = Quiz20.soup_(soup, 'p', 'class', 'artist')
        #Quiz20.dict1(dict, ls1, ls2)
        #Quiz20.dict2(dict,ls1,ls2)
        dt = {i:j for i, j in zip(ls1,ls2)}
        l = [i+j for i,j in zip(ls1,ls2)]
        l2 = list(zip(ls1,ls2))
        d1 = dict(zip(ls1,ls2))
        pprint(dt)
        return dt

        #url='https://music.bugs.co.kr/chart/track/realtime/total'
        #html_doc = urlopen(url)
        #soup = BeautifulSoup(html_doc, 'lxml')
        # print(soup.prettify())
        #titles=soup.find_all('p',{'class':"title"})
        #titles = [i.get_text() for i in titles]
        #print(''.join(i for i in artists))

    @staticmethod
    def quiz25dictcom() -> str:
        '''students = random.sample(my803(),5)
        scores = (myRandom(0, 101) for i in range(5))
        res=dict(zip(students, scores))
        print (res)

        student = random.sample(Quiz00.quiz06memberChoice(), 5)
        score = (myRandom(0, 101) for i in range(5))
        res1 = dict(zip(student, score))
        print(res1)

        ls =  random.sample(my803(),5)
        ls1 = [myRandom(0, 101) for i in range(5)]
        for i in range(5):
            ls.append(Quiz00.quiz06memberChoice())
            ls1.append(myRandom(0, 101))
        res2=dict(zip(ls,ls1))
        print(res2)'''

        q = Quiz00
        s = set(q.quiz06memberChoice() for i in range(5))
        while len(s) !=5:
            s.add(q.quiz06memberChoice())
        students = list(s)
        scores = (myRandom(0,101) for i in range(5))
        #res = {i:j for i, j in zip(students, scores)}
        result = dict(zip(students,scores))
        #print(f'{res}')
        print(f'{result}')
        return result
    def quiz26map(self) -> str: return None

    @staticmethod
    def quiz27melon() -> {}:
        dict = {}
        soup = BeautifulSoup(urlopen(urllib.request.Request('https://www.melon.com/chart/index.htm?dayTime=2022031017',
                                                            headers={'User-Agent': 'Mozilla/5.0'})).read(), 'lxml')
        ls1 = Quiz20.soup_(soup, 'div', 'class', 'ellipsis rank01')
        ls2 = Quiz20.soup_(soup, 'span', 'class', 'checkEllipsis')
        dt={i:j for i, j in zip(ls1, ls2)}
        pprint(dt)
        return dt


    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df =pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')




    '''다음결과 출력
        a   b   c
    1   1   3   5
    2   2   4   6
    '''

    def quiz29_pandas_01(self) -> object:
        d={'a':[1,2],'b':[3,4],'c':[5,6]}
        df=pd.DataFrame

        d1=[]
        d2=[]
        columns=Quiz20.askicode(97,100)
        [d2.append(i) if i % 2==0 else d1.append(i) for i in range(1,7)]
        d = ['1','2']
        d1 =[d1,d2]
        d2=dict(zip(d,d1))
        frame=pd.DataFrame.from_dict(d2, orient='index',columns=columns)
        ic(frame)

        return None


    @staticmethod
    def dict1(dict,ls1,ls2)->{}:
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        pprint(dict)

    @staticmethod
    def dict2(dict,ls1,ls2)->{}:
        for i,j in enumerate(ls1):
            dict[j] = ls2[i]
        pprint(dict)


    @staticmethod
    def rank(soup)-> None:
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(Quiz20.soup_(soup, 'p', 'class', j)):
                print(f'{i}위 : {j}')
            print('#' * 100)


    @staticmethod
    def soup_(soup, point, deep_point, name)->[]:
         return [i.get_text().strip() for i in soup.find_all(point,{deep_point:name})]

    @staticmethod
    def askicode(start,end):
        columns = [chr(i) for i in range(start, end)]
        return columns