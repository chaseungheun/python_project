from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
#컨털 쉬프트 f10 실행

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text) #해당 페이지의 모든 텍스트를 보여줌

soup = bs(html.text,'html.parser')# html이라는 파서로 파싱을 하겠다.
#pprint(soup)
#요소검삼 및 개발자 도구 f12에서 어디부분이 미세먼지부분인지 알아와서 파싱을한다.

#html은 태그div, 속성 class, 속성값 detail_box 로 구성되어있다.
# 속성값은 여러개 가질 수 있다.
#<태그명 속성= "속성값">
#태그, 속성과 속성값 을 넣어준다.
data1 = soup.find('div',{'class':'detail_box'})# 수사망을 좁힌다.
#pprint(data1)#find는 맨 첫번째 탐색되는것만 나온다.
#그래서 findall을 사용한다.

data2 = data1.findAll('dd')
#pprint(data2[0])

find_dust = data2[0].find('span',{'class':'num'})
pprint(find_dust.text)