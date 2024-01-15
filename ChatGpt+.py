from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pathlib
import pyttsx3
import speech_recognition as sr
import warnings

warnings.simplefilter("ignore")

def speak(text):
     #MID=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
     engine = pyttsx3.init()
     FID=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
     engine.setProperty('voice',FID)
     print("")
     print(f"==> GHOKU AI : {text}")
     print("")
     engine.say(text=text)
     engine.runAndWait()

def speechrecognition():
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print('Listening.....')
          r.pause_threshold=1
          audio=r.listen(source,0,0)

     try:
          print('Recognizing.....')
          query=r.recognize_google(audio,language='eng-in')
          return query.lower()

     except:
          return ''
 
ScriptDir=pathlib.Path().absolute()

url="https://flowgpt.com/chat"
chrome_option=Options()
user_agent="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument("----profile-directory=Default")
chrome_option.add_argument(f"user-data-dir={ScriptDir}\\chromedata")
#chrome_option.add_argument("--headless=new")
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=url)
#sleep(100)

chat_num=3

def chat_checker():
     global chat_num
     for i in range(1,1000):
          if i %2 !=0 :
               try:
                    chat_num=str(i)
                    xpatH=f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{i}]/div/div/div/div[1]/p"
                    driver.find_element(by=By.XPATH,value=xpatH)
               except:
                    chat_num=str(i)
                    break

def website_visible():
     while True:
          try:
               xPATH="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea"
               driver.find_element(by=By.XPATH,value=xPATH)
               break
          except:
               pass

# def pop_remover():
#      Xpath="/html/body/div[5]/div[3]/div/section/button"
#      driver.find_element(by=By.XPATH ,value=Xpath).click()

def chat_clean():
     XPath="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/button"
     driver.find_element(by=By.XPATH ,value=XPath).click()

def Send_Message(inputx):
     cht_input="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea"
     driver.find_element(by=By.XPATH,value=cht_input).send_keys(inputx)
     sleep(0.5)
     cht_ky="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button"
     driver.find_element(by=By.XPATH,value=cht_ky).click()

def Msg_Result():
     global chat_num
     chat_num=str(chat_num)
     xpatH=f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{chat_num}]/div/div/div/div[1]/p"
     text=driver.find_element(by=By.XPATH,value=xpatH).text
     new_chat_num =int(chat_num) + 2
     chat_num =new_chat_num
     return text

def Msg_Result_wait():
     sleep(3)
     xpaTH="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/button/p"
     while True:
          try:
               driver.find_element(by=By.XPATH,value=xpaTH)
          except:
               break

website_visible()
chat_checker()

while True:
     query= speechrecognition()
     if len(str(query))<3:
          pass
     elif query == None:
          pass
     else:
          Send_Message(query)
          Msg_Result_wait()
          text=Msg_Result()
          speak(text)
