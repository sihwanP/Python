# --------------------------25.11.11---------------------------------
# a = 0o177
# print(a)
#
# b = 0xABC
# print(b)
#
# c = 2 ** 3
# print(c)
#
# d = 5 / 2
# 정수형끼리 계산을 진행라면 결과가 반드시 정수로 나타난다
# 정수형끼리 계산을 진행하여도 나누어 떨어지지 않으면 실수로 나타난다.
# e = 5 // 2
# print(d)
# print(e)
# f = 5 % 2
# print(f)
#
# a = 8
# a += 1
#
# t = 'dsds"dsds"'
# print(t)
#
# t1 = """안녕하십니까?!!
#         123456789!"""
# print(t1)
#
# t2 = '''123456
#    abcd"efg"'''
# print(t2)

# ///////시퀀스 자료형 : List & Tuple & 딕셔너리
# 시퀀스 : 순서가 중요하다. 순서를 무시할 수 없다.
# [ ] : list 방번호
# ( ) :tuple index
# {key : value} :딕셔너리 0

# a = []
# b = [1, "홍길동", -7.8]
# c = [1, 2, ["life", "is"]]
#
# d = list()

# 인덱스 & 슬라이싱
# e = [1, 2, 3]
# e[0] + e[2]
# e = [1, 2, 3['a', 'b', 'c']]
# print(e[3])

# e = [1, 2, 3, ['a', 'b', ['f', 'c']]]
# print(e[-1][2])

# f[2][2][0]

# a = [1, 2, 3, 4, 5]
# print(a[0:2])
#
# a = "12345"
# print(a[0:2])
#
# b = a[:2]
# print(b)
#
# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[2:5])
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# print((a + b) * 3)
# print(len(a))
#
# print(str(a[2]) + "hi")
# # 3hi

# 값 변경
# a = [6, 1, 5]
# a[2] = 6
# print(a)
# 사용 주의 (되돌리기 불가)
# del a[1]
# print(a)

# 추가
# a.append(3)

# 정렬
# a.sort()

# 원본 라스트의 내부 요소가 정렬된 상태로 다시 재 구성됨

# print(a)
# 변경된 사항을 인지할 방법이 없다.

# 현재 코드가 원본 상태를를 유지하는 것이 맞는가?
# 원본은 그대로 두고 정렬된 결과로 새로운 사본을 만들어서 활용하는 경우가 있을까?

# sorted() : 원래 원본은 그대로 두고, 새롭게 사본은 만든다.

# orininal_list = [9, 2, 7, 8, 1, 5, 3, 4, 6]
# orininal_list.append(4)
#
# orininal_list.reverse()
#
# orininal_list.index(2)
# # 이 위치에 있는 것을 뽑아낸다는 의미

# orininal_list.insert(0, 5)
# orininal_list.sort()
# 중간에 끼워 넣기
# print(orininal_list)


# a = [1, 2, 3, 1, 2, 3]
# # a.remove(3)
# # a.pop(3)  # index
# r = a.count(1)  # 개수세기
# print(r)

# # index 3이 아니라 값이다.
# orininal_list.remove(2)
# # 3의 위치를 날리자!!
# print(orininal_list)
#
# # 끄집어 내기(마지막부터)
# # 방번호
# orininal_list.pop(7)
# print(orininal_list)

# ------------------확장--------------
# a = [1, 2, 3]
# 다른 언어에서는 정대 불가능한 상황
# 배열: 최초로 설정한 요소의 수는 절대 불변.
# a.extend([5, 6])
# a += [5, 6] : 같은 의미
# print(a)

# ------------------------Tuple----------------------
# 튜플 최초 입력 데이터 > 절대 불변
# 튜플은 요소값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일

# print() : 결과 확인용으로 사용하기 때문에 사용 가능.
# t1[1:] <- 이건 원본의 값이 변동되는 것은 아니기 때문에 된다.
# t3 = t1 + t2 <- 원본이 아니라 사본을 만들어서 하는 것이기 때문에 됨.
# t3 = t1*8 <- 위와 같은 이유
# len(t1) <- 길이 확인용

# t1 = ()
# t2 = (1, 2, 3)
# t5 = ('a', 'b', ('ab', 'cd'))
# t3 = (1,) #요소가 1개일 경우.
# t4 = 1, 2, 3 # 이 모양도 튜플로 인지.

# t1 = (1, 2, 'a', 'b')
# # 위 라인은 최초로 튜플을 만든 상황
# del t1[0]
# # 이후에 조작하는 상황
# ------------------------딕셔너리 : {1:N}----------------------

# 딕셔너리 - '연관 배열(associative array)' 또는 `해시(hash)`
# 1 대 n (하나 당 여러 개)
# [{이름:과목 3개} , {이름:과목 3개}, {이름:과목 3개} ]
# 없는 키를 넣으면 추가 됨.

# a = {1: 'a'}
# b[2] = 'b'
# 출력: {1:'a', 2:'b'}

# a['name']='pey'
# {1:'a',2:'b', 'name':'pay'}

# a[3] = [1,2,3]
# {1:'a',2:'b', 'name':'pay', 3:['1','2','3']}

# del(a[1]) : 1이라는 키값와 그것을 물고있는 값을 지움.

# a = {'name': '홍길동', 'phone': '010-0000-0000', 'birth': '0815'}
# a.key()
# 출력: dict_keys(['name','phone','birth'])

# for k in a.keys():
#   print(k)

# list(a.keys()) : 키 값을 뽑아서 리스트 형태로 변환

# a = {'name': '홍길동', 'phone': '010-0000-0000', 'birth': '0815'}
# print(a.items())
# list_of_items = list(a.items())
# print(list_of_items)

# 키와 값의 형태를 새로운 리스트 형태로 변환한다.
# --------------------------------------------------------------
# 전부 날라감
# a.clear()
# a.get('phone')
# # 없는 키를 넣으면 None표기
#
# 'name' in a #true
# 'email' in a #false

# --------------------------------------------------------------
# 집합 set
# 중복을 불가한다, 순서가 없다 - 교집합, 차집합, 합집합

# s1 = set([1, 2, 3])
# print(s1)  # key:value가 아니라서 딕셔너리는 아님
#
# s2 = set("Hello")
# print(s2)
#
# s3 = {1, 2, 3}
# print(s3)
#
# s4 = {'a', 'b', 'c'}
# print(s4)
#
# s5 = set() # 텅 비어있다~
#
# s6 = {}  #태생부터 딕셔너리로 되버림


# 집합의 대상으로 배열을 만드려면 list를 만든 후 변환을 시켜야 한다.
# 다이렉트로 만드는건 안됌
# s1 = set([1, 2, 3])
# l1 = list(s1)
# print(l1[1])


# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# 
# s1 & s2
# # 윗 코드와 아랫 코드 동일한 의미.
# s1.intersection(s2)
# 
# # 합집합
# s1 | s2
# s1.union(s2)
# 
# # 차집합
# s1 - s2
# s1.difference(s2)
# 
# s1.add(9)  # 한번에 한개씩
# print(s1)
# 
# s1.update([5, 6, 7])  # 2개 이상 넣을 경우
# print(s1)
# 
# s1.remove(3) #없는 값을 지우면 에러 발생
# s1.discard(190) #없는 값을 지우는 것.  #없는 값을 지워도 출력
# print(s1)
# 
# s1.clear() #전부 날려버렷!!


# 주머니에 돈이 있으면 택시를 타고 가고,
# 주머니에 돈은 없지만, 카드가 있으면 택시를 타고 가고,
# 돈도 카드도 없으면 걸어가라!
# pocket = ['paper', 'cellphone']
# card = True
#
# if 'money' in pocket:
#   print("택시타고 가라!")
# elif card:
#   print("택시타고 가라!")
# else:
#   print("걸어가라")

# -------------while--------------------------------
# treeHit = 0
# while treeHit < 10:
#   treeHit = treeHit + 1
#   print("나무를 %d 번 찍었습니다!!" % treeHit)
#   if treeHit == 10:
#     print("나무가 넘어갑니다~")
# 출력 형식을 지정한다 > formatter

# number = 0
# while number != 4:
#   print("1. 숫자 1을 선택")
#   print("2. 숫자 2을 선택")
#   print("3. 숫자 3을 선택")
#   print("4. 프로그램 종료")
#
#   user_input = input("숫자를 입력해 주세요.(1부터 4까지): ")
#   number = int(user_input)
#
#   if 1 <= number <= 3:
#     print(" %d 번 을 선택하였습니다." % number)
#   else:
#     print("프로그램 종료합니다.")

# ===============================================================
#
# number = 0
# while number != 4:
#   print("1. 숫자 1을 선택")
#   print("2. 숫자 2을 선택")
#   print("3. 숫자 3을 선택")
#   print("4. 프로그램 종료")
#
#   user_input = input("숫자를 입력해 주세요.(1부터 4까지): ")
#   number = int(user_input)
#
#   if 1 <= number <= 3:
#     print(" %d 번 을 선택하였습니다." % number)
#   else:
#     print("프로그램 종료합니다.")

# ===============================================================
# number = 0
# while number != 4:
#   try:
#     print("1. 숫자 1을 선택")
#     print("2. 숫자 2을 선택")
#     print("3. 숫자 3을 선택")
#     print("4. 프로그램 종료")
#
#     user_input = input("숫자를 입력해 주세요.(1부터 4까지): ")
#     number = int(user_input)
#
#     if 1 <= number <= 3:
#       print(" %d 번 을 선택하였습니다." % number)
#     elif number != 4:
#       print("잘못된 숫자입니다. 정확한 숫자를 눌러주세요.")
#   except ValueError:
#     print("잘못된 입력 > 숫자로 입력해주세요.")
#
# print("종료되었습니다.")
# #
# # # try,  예외처리: Exception


# 커피가 있으면 계속 추출
# 커피가 마감될 때 정지
# 한 잔당 가격, 재고 량
# coffee = 10
# while True:
#   money = int(input("돈 내놔!!: "))
#   if money == 300:
#     print("커피를 준다.")
#     coffee = coffee - 1
#   elif money > 300:
#     print("거스름돈 %d 를 주기!! 커피 주기" % (money - 300))
#     coffee = coffee - 1
#   else:
#     print("돈을 더 내놔라!!")
#     print("남은 커피는 %d 개 입니다." % coffee)
#   if coffee == 0:
#     print("재고 없음!!")
#     break

# ===============================================================
# For
# test_list = ['one', 'two', 'three']
#
# for i in test_list:
#   print(i)

# a = [(1, 2), (3, 4), (5, 6)]
# for (f, s) in a:
#   print(f + s)

# 총 5명의 학생이 시험을 본다
# 시험 점수가 60점 이상 합격,
# 그렇지 않으면 불합격이다.
# 합격인지, 부합격인지 결과를 도출 해내시오.
# 출력 : 학생들의 일련번호도 같이 출력하시오.

# marks = [90, 25, 67, 45, 80]
# no = 0
# for s in marks:
#   no = no + 1
#   if s < 60:
#     continue
#   print("%d 번 학생은 합격" % no)

# continue : 이 문구를 실행하면 그 이하 코드는 무시하고, 다시 반복의 시작으로 돌아간다.
# 위 프로그램에서 불합격인 경우에는 아무런 문구를 출력하지 않는다
# 1~10 하면 55

# add = 0
# for i in range(1, 11):
#   add = add + i
#   print(add)

# add = 0
# for i in range(1, 11):
#   add += (1 / i)
# print(add)
