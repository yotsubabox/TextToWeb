import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

currnetDirctory = os.path.dirname(os.path.realpath(__file__)) # 소스코드가 있는 디렉토리 경로

text = open(currnetDirctory + "/새 텍스트 문서.txt" , 'r') # 텍스트 파일 읽어옴
originUrl = text.readlines()
text.close()

urls = []

def remove_values_from_list(the_list, val): # 특정 요소 전부 제거
   return [value for value in the_list if value != val]

def list_to_str(list): # list요소 str로 반환
    return ''.join(list)

for i in originUrl: # 공백 제거
    urls.append(i.splitlines())

urls = remove_values_from_list(urls, ['']) # 공백 요소 제거

print(urls)

################## 셀레니움 시작
driver = webdriver.Chrome(currnetDirctory + '/chromedriver.exe')
driver.get(list_to_str(urls[0]))
time.sleep(1)

for i in urls[1:]: # 시작 1부터
    driver.execute_script("window.open('"+list_to_str(i)+"');")
    time.sleep(1)
    # print(list_to_str(i))

sys.exit()
