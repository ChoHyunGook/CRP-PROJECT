from matplotlib import rc, font_manager

from context.domains import Dataset
from context.models import Model
from titanic import TitanicModels
from icecream import ic
import matplotlib.pyplot as plt #시각화
import seaborn as sns
rc('font',family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())
'''
데이터 시각화
엔터티(개체)를 차트로 표현하는것

모든 feature 를 다 그려야 하지만, 시간관계상
survived, pclass, sex, embarked 의 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오.
'''

class TitanicTemplate(object):
    dataset = Dataset()
    model=Model()
    def __init__(self,fname):
        self.entity = self.model.new_model(fname)
        this=self.entity
        ic(f'트레인 타입: {type(this)}')
        ic(f'트레인 컬럼: {this.columns}')
        ic(f'트레인 상위5행: {this.head()}')
        ic(f'트레인 하위5행: {this.tail()}')

    def matplot_visualize(self)->None:
        this=self.entity
        #self.draw_survived(this)
        #self.pclass(this)
        #self.sex(this)
        self.embarked(this)
        #plt.show(this)

    @staticmethod
    def draw_survived(this)->None:
        f , ax=plt.subplots(1, 2, figsize=(18,8))  # nrows=1, ncols=2, figsize=18inch,8inch
        this['Survived'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%', ax=ax[0],shadow=True)
        ax[0].set_title('0.사망자 vs 1. 생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1. 생존자')
        sns.countplot('Survived',data=this,ax=ax[1])
        #plt.show()
        #print(f'{this.sname}')
        model=Model()
        plt.savefig(f'{model.get_sname()}draw_survived.png')

    @staticmethod
    def pclass(this)->None:
        this['생존결과'] = this['Survived'] \
            .replace(0, '사망자').replace(1, '생존자')
        this['Pclass'] = this['Pclass'].replace(1, '1등석').replace(2, '2등석').replace(3, '3등석')
        sns.countplot(data=this)
        #plt.show()
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_pclass.png')

    @staticmethod
    def sex(this)->None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0],
                                                                        shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1],
                                                                          shadow=True)
        ax[0].set_title('남성의 생존비율 [0.사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0.사망자 vs 1.생존자]')
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_sex.png')
        #plt.show()
    @staticmethod
    def embarked(this)->None:
        this['생존결과'] = this['Survived'] \
            .replace(0, '사망자').replace(1, '생존자')
        this['승선항구'] = this['Embarked'] \
            .replace("C", '쉘버그').replace("S", '사우스햄톤').replace("Q", '퀸즈타운')
        sns.countplot(data=this)
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_embarked.png')
        #plt.show()