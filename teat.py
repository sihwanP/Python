# a, b = map(int, input("두 개의 정수 입력: ").split('+'))
# result = (a + b)
# print(result)
# # map (a, b)
# # a : 마법 주문
# # b: 주문을 걸 대상
# print("=" * 50)
#
# print(3, 7, 8, sep='-')

# 연습 문제
# 세 개의 문자열(0~9로만 구성)을 키보드로 입력하기
# 입력 시점에서 '-'기호를 기준으로 분리하기
# 출력 시점에서 '-'를 붙여서 출력하기
# a, b, c = input('키보드 입력하기: ').split('-')
# print(a, b, c, sep='\t')

# print(1, end='')
# print(2, end='')
# print(3, end='')
# print(1)

# x = input().split()
# print(x)


# a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# 30 in a
# 100 not in a

# q = list(range(0, 10)) + list(range(20, 20))

# a = [0, 10, 20, 30]
# a.__gititem__(1)
# a[1]

# 음수
# a = [0, 10, 20, 30, 40]
# a[-1]

# a = [38, 21, 53, 62, 19]
# len(a)
# a = [len(a) - 1]
# 맨 마지막 위치


# 슬라이스 - 시퀀스
# a = [38, 21, 53, 62, 19, 53, 62, 19]
# a[0:4] # 0부터 4의 직전 3까지
# # a[1:1] => [] : 빈 상태로 만듦
# a[1:2] #10
# a[4:7] #19, 53, 62
# a[4:-1] #19, 53, 62
# a[2:8:3] # 2~7까지 3씩 증가

# numbers = [10, 7, 1, 4, 2]
#
# print("정렬 전 리스트:", numbers)
#
# for i in range(len(numbers) - 1):
#   min_index = i
#   for j in range(i + 1, len(numbers)):
#     if numbers[j] < numbers[min_index]:
#       min_index = j
#
#   if min_index != i:
#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
#
# print("오름차순 정렬 후 리스트 (선택 정렬):", numbers)


# 딕셔너리 @@?
# { ~ : ~ }사용 = 1:n(다수)
# lux = {'health': 500, 'health': 950, 'mana': 900, 'melee': 558, 'armor': 18.72}
# print(lux)

# # key 이름이 중복되면?
# print(lux['health'])
# x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
# x = {[17, 20]: 100}
# x = {}
# y = dict(health=500, mana=900, melee=558, armor=18.72)


# lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [500, 900, 558, 18.72]))
# lux2['health'] = 9999
# lux2['mana'] = 9999
#
# lux2['mana_regen'] = 3.2  # 추가됨
# # lux2['attack_speed']
#
# print('health' not in lux2) #False
# print(len(lux2)) #5

# x = 10
# if x == 10:
#   print("Hello World!!")
#
# print("Hello World!!")
# 출력: Hello World!!
# 출력:  Hello World!!

# File "<stdin>", line2 : 이 부분에서 잘못 됫다는 것을 알려주는 코드.

# x = 10
# if x == 7:
#   pass  # 개발도중 쓸 코드가 없을 시 사용하는 코드.(빼면 에러뜸)

# TODO(= 상대가 무언가를 하기 위해서 작성 된 공간. )
# TODO는 해야 할 일이라는 뜻인데, 보통 주석에 넣는다.
# 이렇게 TODO를 넣어 두면 검색으로 쉽게 찾을 수 있다.
# 그래서 프로그래머들은 주석에
# TODO 이외에도 FIXME, DEBUG, NOTE등과 같이 코드는 아니지만 일관된 주석을 사용한다.
# 논리적 에러(문법적인 오류)
# (DEBUG)실행 에러(실행했더니 나의 의도와 다르게 나오는 결과(에러 문제는 없음.)
#  ㄴ> 찾는 방법 : 한 라인 씩 실행 시켜서 찾는 방법 뿐임.
