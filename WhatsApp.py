from newsapi import NewsApiClient #Import
from selenium import webdriver #Import
import random
import time

Driver = webdriver.Firefox()   #To open Firefox through webdriver
Driver.get('https://web.whatsapp.com')  #Use the driver to get to the URL

NewsAPI = NewsApiClient(api_key='e3fb0a59b3f64cedbea1c1a2ff5a9df1') #Check the API Key

def RandomY():
    global Articles  #To consider the outer Articles variable

    String = ['bbc-news', 'bloomberg', 'buzzfeed']  #To store the Sources in the List

    Y = random.randint(0,2)  #To randomise the Sources list

    Top_Headlines = NewsAPI.get_top_headlines(sources=String.pop(Y))  #Get the Top Headlines from the Source i.e. BBC News and Pop as it is list

    Articles = Top_Headlines['articles'] #To get into Articles of the Top_Headlines

def RandomX():
    global Articles         #To consider the outer Articles variable
    global Message

    X = random.randint(0,5) #To generate random values of X
    ArticlesP = Articles[X]  #To get to news 0 of the Articles
    Message = ArticlesP['title'] + " "+ArticlesP['url']  #To get to the Title and URL

Name = input('Enter the Name : ')       #The Name of the Contact
Count = int (input('Count : '))               #Number of times to be sent

input('Start')                   #To wait for Scanning

ContactElement = Driver.find_element_by_xpath('//span[@title = "{}"]'.format(Name))  #To get to the Contact Element
ContactElement.click()  #To click on that Contact

MessageBoxElement = Driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]')  #To get to the Message Box Element

for i in range(Count):  #Loop
    RandomY()
    RandomX()

    MessageBoxElement.send_keys(Message)  #To send the Message to the Message Box

    time.sleep(5)

    SendButtonElement = Driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/footer/div[1]/div[3]/button')  #To get to the Send Button Element
    SendButtonElement.click()  #To Click on the Send Button

