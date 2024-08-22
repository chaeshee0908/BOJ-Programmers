# import pickle

# a = [1,2,3,4,5]
# # a_list.dat이름으로된 파일을 열어 쓰기작업(파일만들기)
# f = open('a_list.dat','wb')
# # a를 f에다 쏟아버리겠다
# pickle.dump(a, f)
# f.close()

# # a_list.dat이름으로된 파일을 열어 읽기작업(binary로 읽음)
# f = open('a_list.dat', 'rb')
# # data에 f의 데이터를 복사
# data = pickle.load(f)
# f.close()
# print(data)

# import random

# # 0~1 까지 아무숫자
# print(random.random())
# # 1부터 3포함해서 아무 정수
# print(random.randint(1,3))
# a = [1,2,3,4,5,6,7,8,9]
# # 배열 a를 섞어준다
# random.shuffle(a)
# print(a)
# # a중 3개를 아무거나 뽑아줌
# print(random.sample(a,3))

# # sample 함수를 이용한 로또 번호 추첨
# lotto = [i for i in range(1, 46)]
# lotto_n = random.sample(lotto, 6)
# lotto_n.sort()
# print('lotto num :', lotto_n)
# print(sorted(random.sample(range(1,46),6)))

# 클래스 : 함수들을 저장해놓는 주머니
# 클래스 : 붕어빵 만드는 틀
class Bank:
    def __init__(self):
        self.money = 0
    def deposit(self, a):
        self.money += a

person1 = Bank()    # Bank라는 클래스를 사용할 수 있는 권한을 person1에게 준것
person1.deposit(50000)
person2 = Bank()
person2.deposit(100000)
print(person1.money)
print(person2.money)
person3 = Bank()
print(person3.money)

# Bank에서 제공하는 모든 서비스를 상속받는다
class Bank2(Bank):
    pass

person4 = Bank2()
print(person4.money)
person4.deposit(30000)
print(person4.money)
