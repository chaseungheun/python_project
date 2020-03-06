from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

def naverCorona():
    html = requests.get('https://search.naver.com/search.naver?query=코로나')

    soup = bs(html.text,'html.parser')

    data1 = soup.find('div',{'class':'graph_view'})
    data2 = data1.findAll('strong',{'class':'num'})

    pprint(data2[0].text)# 확진환자
    pprint(data2[1].text)# 격리해제
    pprint(data2[2].text)# 검사진행
    pprint(data2[3].text)# 사망자
    return data2
