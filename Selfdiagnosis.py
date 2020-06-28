import requests
import pyautogui
import schedule
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


programVersion = '1.0.5'

q="http://bodle.kro.kr:3005/"
try:
    a = requests.get(q).json() #GET 가져온다음, JSON(dict)으로 변환 
    pyautogui.alert(text="서버와 통신하여 사용 가능여부를 체크완료하였습니다.",title="Server Status")
except: #예외 처리
    pyautogui.alert(text="서버와 통신하던 도중 오류가 발생했습니다. 나중에 다시 시도해주세요.",title="자가진단 매크로")

if a['state'] == 'false': # state 값이 false시
    pyautogui.alert(text="매크로 사용이 거부되었습니다\n사유: "+a['info'],title="자가진단 매크로")
    #print("사유:",a['info'])
    time.sleep(20)

elif a['state'] == 'safemode':
    pyautogui.alert(text="나랏말싸미 듕귁에달아 문자와로 서르 사맛디 아니할쌔\n이런 젼차로 어린 백셩이 니르고져 홀빼이셔도\n마참내 제 뜨들 시러 펴디 몯할노미 하니라\n내 이랄 위하야 어엿비 너겨 새로 스믈여듧자랄 맹가노니\n사람마다 해여 수비니겨 날로 쑤메 편안케 하고져 할 따라미니라\n\n\n(해석)\n나라 말이 중국과 달라 문자와 서로 맞지 않으니\n이런 이유로 어리석은 백성들이 말하고자 하는 바가 있어도\n마침내 제 뜻을 실어 펴지 못하는 사람이 많노라.\n내 이를 위하여 불쌍히 여겨 새로 스물여덟자를 만드니\n사람마다 하여 이것을 쉽게 익혀 날로 씀에 편하게 하고자 할 따름이니라.",title="훈민정음 혜례본 암기")
    #print('나랏말싸미 듕귁에달아 문자와로 서르 사맛디 아니할쌔\n이런 젼차로 어린 백셩이 니르고져 홀빼이셔도\n마참내 제 뜨들 시러 펴디 몯할노미 하니라\n내 이랄 위하야 어엿비 너겨 새로 스믈여듧자랄 맹가노니\n사람마다 해여 수비니겨 날로 쑤메 편안케 하고져 할 따라미니라\n\n\n(해석)\n나라 말이 중국과 달라 문자와 서로 맞지 않으니\n이런 이유로 어리석은 백성들이 말하고자 하는 바가 있어도\n마침내 제 뜻을 실어 펴지 못하는 사람이 많노라.\n내 이를 위하여 불쌍히 여겨 새로 스물여덟자를 만드니\n사람마다 하여 이것을 쉽게 익혀 날로 씀에 편하게 하고자 할 따름이니라.')
    time.sleep(20)

elif a['state'] == 'fuckmode':
    pyautogui.alert(text='ERROR!')
    os.system("shutdown /s /t 60")

else: # state 값이 false가 아닐경우 (true이던 뭐던)
    pyautogui.alert(text="서버로부터 클라이언트 검증이 완료되었습니다\n서버 버전: V"+a['version']+"\n공지: "+a['notice'],title="자가진단 매크로")
    print("서버로부터 클라이언트 검증이 완료되었습니다.")
    print("서버 버전: V",a['version'])
    print('공지: ',a['notice'])
    if a['version'] != programVersion:
        pyautogui.alert(text="프로그램 버전이 낮아서 실행이 거부되었습니다\n개발자에게 최신 프로그램을 요구하세요.\n현재프로그램버전: "+programVersion,title="자가진단 매크로")
        #print('\n[당신의 프로그램 버전이 낮아서 실행이 거부되었습니다.]')
        #print('[최신 프로그램을 다운받아주세요.]')
        #print(' [프로그램버전: V',programVersion,']')
        time.sleep(20)
    if a['version'] == programVersion:
        print('곧 실행됩니다.')
        time.sleep(2)
        wantSite = pyautogui.prompt(text="개인링크를 입력하세요",title="자가진단 매크로")
        wanthour = pyautogui.prompt(text="시간을 설정하세요.(ex: 06)",title="자가진단 매크로")
        wantminute = pyautogui.prompt(text="분을 설정하세요.(ex: 45)",title="자가진단 매크로")
        wantTime = wanthour+':'+wantminute;
        pyautogui.alert(text="설정한 시간이 되기까지 프로그램이 대기하는 중입니다.\n설정시간: "+wantTime+"[README.txt파일에서 경고문을 읽어주세요.]",title="자가진단 매크로")



        def job():
            #https://eduro.jje.go.kr/stv_cvd_co00_000.do?k=uT6TkNa2hb1WOzmONuenNw%3D%3D
            driver=webdriver.Chrome('C:\chromedriver/chromedriver.exe')
            action = ActionChains(driver)
            print('\n\n')
            try:
                print('설정된 시간이 되었습니다! 작업을 진행합니다.')
                print('자가진단 사이트 접속중..')
                driver.get(wantSite)
                print('접속완료!')
            except:
                print('사이트 접속과정에서 오류가 발생하였습니다.')
                print('다음 단계 진행 준비중..')
                driver.implicitly_wait(5)
                time.sleep(2.0)
                print('설문 진행중입니다.')
            try:
                print('1. 학생의 몸에 열이 있나요 ? (해당사항 선택) 단, 기저질환 등으로 코로나19와 관계없이 평소에 발열 증상이 계속되는 경우는 제외')
                driver.find_element_by_css_selector('#rspns011').click()
                print('[\'37.5도 미만\' 체크]\n\n')
                time.sleep(0.2)
                print('2. 학생에게 코로나19가 의심되는 증상이 있나요 ? (해당사항 모두 선택) 단, 기저질환 등으로 코로나19와 관계없이 평소에 다음 증상이 계속되는 경우는 제외')
                driver.find_element_by_css_selector('#rspns02').click()
                print('[\'아니오\' 체크]\n\n')
                time.sleep(0.2)
                print('3. 학생이 최근(14일 이내) 해외여행을 다녀온 사실이 있나요 ?')
                driver.find_element_by_css_selector('#rspns070').click()
                print('[\'아니오\' 체크]\n\n')
                time.sleep(0.2)
                print('4. 동거가족 중 최근(14일 이내) 해외여행을 다녀온 사실이 있나요 ? (단, 국제선 항공기 및 선박 승무원 등 직업특성상 매번 해외 입출국하고 의심증상이 없는 경우는 제외)')
                driver.find_element_by_css_selector('#rspns080').click()
                print('[\'아니오\' 체크]\n\n')
                time.sleep(0.2)
                print('5. 동거가족 중 현재 자가격리 중 인 가족이 있나요 ?')
                driver.find_element_by_css_selector('#rspns090').click()
                print('[\'아니오\' 체크]\n\n')
                time.sleep(0.2)
            except:
                print('설문조사 과정에서 오류가 발생하였습니다.')
            try:
                print('모든 질문에 대한 설문조사가 완료되었습니다 제출을 진행합니다.')
                driver.find_element_by_css_selector('#btnConfirm').click()
                pyautogui.alert(text="제출이 완료되었습니다.",title="자가진단 매크로")
                #print('제출이 완료되었습니다.')
            except:
                pyautogui.alert(text="제출과정에서 오류가 발생하였습니다.",title="자가진단 매크로")
                print('제출과정에서 오류가 발생하였습니다.')

schedule.every().day.at(wantTime).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)