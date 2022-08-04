import numpy as np
import pandas as pd
from icecream import ic
from sklearn import preprocessing

from context.domains import Dataset
from context.models import Model
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier #분류(classifier)-범주냐
from sklearn.ensemble import RandomForestRegressor #회귀(Regression)-하나의값을 원하냐


class TitanicModels(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',
                   'Cabin', 'Embarked']
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        # Entity 에서 Object 로 전환
        this = self.drop_feature(this, 'Ticket','Cabin')
        # self.kwargs_sample(name='이순신') kwargs 샘플... 타이타닉 흐름과 무관
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        this = self.family_ordinal(this)
        this = self.drop_feature(this, 'SibSp', 'Parch')
        #this = self.cabin_ratio(this)
        #this = self.drop_feature(this,'Cabin')
        # self.df_info(this)
        k_fold = self.create_k_fold()
        accuracy = self.get_accuracy(this, k_fold)
        ic(accuracy)
        return this

    def learning(self, train_fname, test_fname):
        this = self.preprocess(train_fname, test_fname)
        print('*'*100)
        self.df_info(this)
        k_fold = self.create_k_fold()
        ic(f'사이킷런 알고리즘 정확도: {self.get_accuracy(this, k_fold)}')
        self.submit(this)

    @staticmethod
    def submit(this):
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./save/submission2.csv', index=False)

    @staticmethod
    def id_info(this):
        ic(f'id 의 타입  {type(this.id)}')
        ic(f'id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    # 결합도는 낮추고 응집도는 높일수록 이상적인 모듈화가 이루어진다

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def drop_feature(this, *feature) -> object:
        # ic(type(feature)) # ic| type(feature): <class 'tuple'>
        '''
        for i in [this.train, this.test]:
            for j in feature:
                i.drop(j, axis=1, inplace=True)'''
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]
        # [i.drop(list(feature), axis=1) for i in [this.train, this.test]]
        return this

    '''categori=>
        nominal(이름) vs ordinal(순서)
        quantitative=>(숫자)
        interval(상대) vs ratio(절대적인기준)'''

    @staticmethod
    def extract_title_from_name(this) -> None:
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)
        # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        a = list(set(a))
        # print(f'>>> {a}')
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_maping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_maping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)  # 왜 NaN 값에 -0.5 를 할당할까요 ?
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # 이것을 이해해보세요
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['Age'] = pd.cut(these['Age'], bins=bins, labels=labels)  # pd.cut() 을 사용
            these['AgeGroup'] = these['Age'].map(age_mapping)  # map() 을 사용
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        '''this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)'''
        bins = [-1, 8, 15, 31, np.inf]
        fare_mapping = {1, 2, 3, 4}
        for these in [this.train, this.test]:
            these['FareBand'] = these['Fare'].fillna(1)
            these['FareBand'] = pd.qcut(these['FareBand'], 4, fare_mapping)
            # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
        return this

    @staticmethod
    def family_ordinal(this)->object:
        for these in [this.train,this.test]:
            these['Family'] = these['SibSp'] + these['Parch']
        return this

    @staticmethod
    def cabin_ratio(this)->object:
        cabin_mapping={'A':0,'B':0.4,'C':0.8,'D':1.2,'E':1.6,'F':2,'G':2.4,'T':2.8}
        for these in [this.train,this.test]:
            these['Cabin']=these['Cabin'].fillna('N',inplace=True)
            these['Cabin']=these['Cabin'].str[:1]
            #these['Cabin_Map']=these['Cabin'].map(cabin_mapping)
            le = preprocessing.LabelEncoder()
            le = le.fit(this['Cabin'])
            this['Cabin'] = le.transform(this['Cabin'])
        return this

    @staticmethod
    def create_k_fold() -> object:  # 시험문제
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this, k_fold):  # 시험점수
        score = cross_val_score(RandomForestClassifier(), this.train, this.label,
                                cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))
        {print(''.join(f'key:{i},val:{j}')) for i, j in kwargs.items()}  # key:name,val:이순신
