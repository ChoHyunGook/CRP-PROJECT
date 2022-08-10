from hello.domains import myRandom, my803, Member
import random

class Quiz00:
    def quiz00calculator(self):
        n1 = myRandom(1, 100)
        n2 = myRandom(1, 100)
        o = ['+', '-', '*', '/', '%']
        op = o[myRandom(0, 4)]

        if (op == '+'):
            res = n1 + n2
        elif (op == '-'):
            res = n1 - n2
        elif (op == '*'):
            res = n1 * n2
        elif (op == '/'):
            res = n1 / n2
        elif (op == '%'):
            res = n1 % n2

        return print(f'{n1} {op} {n2} = {res}')

    def quiz01bmi(self):
        this = Member()
        this.name = my803()
        this.inch = myRandom(120, 200)
        this.weight =myRandom(40, 120)
        bmi = this.weight / (this.inch * this.inch / 10000)
        name = this.name[myRandom(0, 4)]
        if bmi <= 18.0:
            res = '저체중'
        elif bmi <= 22.9:
            res = '정상'
        elif bmi <= 23.0:
            res = '과체중'
        elif bmi <= 24.9:
            res = '위험체중'
        elif bmi <= 29.9:
            res = '결과: 1단계 비만'
        elif bmi <= 34.9:
            res = '결과: 2단계 비만'
        elif bmi < 35:
            res = '결과: 고도 비만'
        return print(f'이름:{name}\n 키:{this.inch}\n 몸무게:{this.weight}\n Bmi지수:{bmi}\n 결과:{res} ')

    def quiz02dice(self):
            dice1 = myRandom(1, 6)
            dice2 = myRandom(1, 6)
            if dice1 > dice2:
                res = f'1번 주사위{dice1}\n 2번주사위:{dice2}\n 1번 주사위가 {dice1 - dice2}차이로 이겼다'
            elif dice1 < dice2:
                res = f'1번 주사위: {dice1}\n 2번주사위: {dice2}\n2번 주사위가 {dice2 - dice1}차이로 이겼다'
            else:
                res = f'1번주사위: {dice1}\n 2번주사위: {dice2}\n 비겼다'
            return print(res)

    def quiz03rps(self):
            c = myRandom(0, 2)
            p = myRandom(0, 2)
            rps = ['가위', '바위', '보']

            if p - c == 2 or c - p == -1:
                res = 'WIN'
            elif p - c == 1 or c - p == -2:
                res = 'LOSE'
            elif p - c == 0:
                res = 'DRAW'
            return print(f'플레이어: {rps[p]}\n 컴퓨터:{rps[c]}\n 결과: {res}')

    '''
    <게이머 승리일때>
     컴퓨터0(가위) / 게이머1(바위)(win) = -1
     컴퓨터1(바위) / 게이머2(보)(win) = -1
     컴퓨터2(보) / 게이머0(가위)(win) = 2
    <컴퓨터 승리일때>
     컴퓨터0(가위) / 게이머2(보)(lose) = -2
     컴퓨터1(바위) / 게이머0(가위)(lose) = 1
     컴퓨터2(보) / 게이머1(바위)(lose) = 1 '''

    def quiz04leap(self):
        y = myRandom(1900, 2022)
        s=f'{y}년은 윤년' if (y % 4 == 0 and not y % 100 == 0 or y % 400 == 0) else f'{y}년은 평년'
        return print(s)

    def quiz05grade(self):
        name = my803()
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        total = kor + eng + math
        avg = total / 3

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 65:
            grade = 'D'
        elif avg >= 60:
            grade = 'E'
        else:
            grade = 'F'

        if grade =='F':
            grpass = '불합격'
        else:
            grpass = '합격'


        return print(f'########## 성적표 ########\n '
                     f'* 이름: {name}\n  '
                     f'* > 국어: {kor}점\n  '
                     f'* > 영어: {eng}점\n" '
                     f'* > 수학: {math}점\n '
                     f'* 총점: {total}점\n '
                     f'* 평균(정수): {avg}점\n'
                     f'* 학점: {grade}\n'
                     f'합격여부: {grpass}\n'
                     '* #######################')
    @staticmethod
    def quiz06memberChoice():
        members = my803()
        return members[myRandom(0, 23)]

    def quiz07lotto(self):

        lotto = random.sample(range(1, 45), 6)
        return lotto.sort()

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        ''' total = 100000
                while 1:
                    menu = int(input('사용하실 메뉴를 선택해 주세요\n'
                                     '0.종료 1.잔액조회 2.현금인출 3.입금'))
                    if menu == 0:
                        return ('종료')
                    if menu == 1:
                        print(f'{total}')
                    elif menu == 2:
                        output = int(input('출금하실 금액'))
                        if total >= output:
                            total = total - output
                            print(f'인출금액: {output}\n 잔액: {total}')
                        elif total < output:
                            print('잔액이 부족합니다.')
                    elif menu == 3:
                        inp = int(input('입금하실 금액'))
                        total = inp + total
                        print(f'입금 금액:{inp} 잔액:{total}')'''

        return Account.main()


    def quiz09gugudan(self):  # 책받침구구단
        res = ""
        for i in [2, 6]:
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        return print(res)


class Account(object):
    def __init__(self,name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = my803()[myRandom(0,23)] if name == None else name
        self.account_number=self.creat_account_number() if account_number ==None else account_number
        self.money=myRandom(100,999) if money == None else money

    def to_String(self):
        return f'은행: {self.BANK_NAME}\n' \
               f'입금자:{self.name}\n' \
               f'계좌번호:{self.account_number}\n' \
               f'입금금액:{int(self.money)}'

    @staticmethod
    def creat_account_number():
        '''ls=[str(myRandom(0,10)) for i in range(3)]
        ls.append("-")
        ls += [str(myRandom(0, 10)) for i in range(2)]
        ls.append("-")
        ls += [str(myRandom(0, 10)) for i in range(6)]'''
        return "".join(["-" if i==3 or i==6 else str(myRandom(0, 10)) for i in range(13)])

    @staticmethod
    def del_account(ls,accout_number):
        for i,j in enumerate(ls):
            if j.account_number==accout_number:
                del ls[i]

    @staticmethod
    def find_account(ls,account_number):
       '''return ''.join([j.to_String() if j.account_number==account_number else '해당계좌가 없습니다' for i,j in enumerate(ls)])'''
       for i,j in enumerate(ls):
            if j.account_number==account_number:
                ls[i].to_String()
                return ls[i]


    @staticmethod
    def deposit_money(ls,account_number,deposit):
        for i,j in enumerate(ls):
            if j.account_number == account_number:
                  ls[i].money += deposit
                  return ls[i]



    @staticmethod
    def minus_money(ls,account_number,minus):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                ls[i].money -= minus
                return ls[i]




    @staticmethod
    def main():
        ls=[]
        while 1:
            menu= input('0.종료 1. 계좌계설 2.계좌목록 3. 입금 4. 출금 5. 계좌해지 6. 계좌조회')
            if menu == '0':
                break
            if menu == '1':
                acc=Account(None,None,None)
                print(f'{acc.to_String()}가 개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a='\n'.join(i.to_String() for i in ls)
                print(a)
            elif menu == '3':
                res=Account.deposit_money(ls,input('입금할 계좌번호'),int(input('입금하실 금액')))
                print(f'{res.to_String()}')

            elif menu == '4':
                res=Account.minus_money(ls,input('출금할 계좌번호'),int(input('출금하실 금액')))
                print(f'{res.to_String()}')

            elif menu == '5':
                Account.del_account(ls,input('탈퇴할 계좌번호'))
                print(f'해지되셨습니다. 그동안 이용해주셔서 감사합니다')

            elif menu == '6':
                res=Account.find_account(ls,input('조회할 계좌번호'))
                print(f'{res.to_String()}')

            else:
                print('Wrong Numbver... Try Again')
                continue
