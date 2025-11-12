# json 파일 형식
# books = [
#   {
#     "제목": "열심히 공부하자!",
#     "가격": 19000
#   },
#   {
#     "제목": "와우",
#     "가격": 18000
#   },
#   {
#     "제목": "놀자",
#     "가격": 38000
#   }
# ]
#
# print("가장 저렴한 책")
# print(min(books, key=itemgetter("가격")))
# 모듈을 읽어 들입니다.
from urllib import request

from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾습니다.
for location in soup.select("location"):
  # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
  print("도시:", location.select_one("city").string)
  print("날씨:", location.select_one("wf").string)
  print("최저기온:", location.select_one("tmn").string)
  print("최고기온:", location.select_one("tmx").string)
  print()
