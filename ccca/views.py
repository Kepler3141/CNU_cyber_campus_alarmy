from django.shortcuts import render
import sys, os
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common import db


# def index(request):
#     return render(request, 'ccca/ccca.html')

def read_material_data():
    driver.find_element(By.XPATH, '//*[@id="sidebarHomeAlarm_2"]/ul/li[3]/a').click()  # 자료실 클릭
    time.sleep(3)
    material_list = driver.find_element(By.XPATH, '//*[@id="listBody"]').text  # 자료 읽기
    material_list = list(zip(material_list.split('\n')[::4], material_list.split('\n')[1::4]))
    return material_list

def read_homework_data():
    driver.find_element(By.XPATH, '//*[@id="sidebarHomeAlarm_2"]/ul/li[4]/a').click()  # 과제 클릭
    time.sleep(3)
    homework_list = driver.find_element(By.XPATH, '//*[@id="tbody"]').text  # 과제 읽기
    homework_list = list(zip(homework_list.split('\n')[::5], homework_list.split('\n')[1::5], homework_list.split('\n')[2::5]))
    return homework_list


def main(request):
    driver = webdriver.Chrome()
    url = 'https://dcs-lcms.cnu.ac.kr/login?redirectUrl=https://dcs-lcms.cnu.ac.kr/'
    driver.get(url)

    driver.maximize_window()
    # 로그인 시작
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[3]/div/form/div/div[1]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="drawUniv_list"]/li[4]/a/span[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[3]/div/form/div/div[2]/input[1]').send_keys(
        f.readline()[:-1])
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[3]/div/form/div/div[2]/input[2]').send_keys(
        f.readline())
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[3]/div/form/div/div[2]/button').click()
    time.sleep(20)
    # 로그인 완료

    driver.find_element(By.XPATH,
                        '//*[@id="wrapper"]/div[2]/div/div/div[3]/div/div[2]/ul/li/button').click()  # 강의실 버튼 클릭
    time.sleep(3)

    data = dict()

    # 1번째 강의 시작
    driver.find_element(By.XPATH, '//*[@id="cardList"]/div[1]/div/div/ul/li[1]').click()  # 1번째 강의 클릭
    time.sleep(3)

    print(read_material_data())
    print(read_homework_data())
    # 1번째 강의 완료

    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/ul[2]/li[1]/a').click()  # 강의실 클릭
    time.sleep(3)

    # 2번째 강의 시작
    driver.find_element(By.XPATH, '//*[@id="cardList"]/div[2]/div/div/ul/li[1]').click()  # 2번째 강의 클릭
    time.sleep(3)

    print(read_material_data())
    print(read_homework_data())
    # 2번째 강의 완료

    time.sleep(1000)
    return render(request, 'ccca/main.html', {'testdata': testdata})


def notifications(request):
    return render(request, 'ccca/notifications.html')


def assignments(request):
    return render(request, 'ccca/assignments.html')


def materials(request):
    return render(request, 'ccca/materials.html')