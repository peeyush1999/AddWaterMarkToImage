#script to fill gform

import time
import pyautogui
import threading
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import random
import string


def randomString(stringLength=15):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def phone():
    lst = [1,2,3,4,5,6,7,8,9,0]

    i=0
    num=0
    while(i<10):
        if(i==0):
            num = num+9
        else:
            num = num*10 + random.choice(lst)
        i+=1
    return num
        
    
driver = webdriver.Chrome(executable_path=r'D:/webdrivers/chromedriver.exe')    
branch=['CSE','ME','CE','EC','EE','MBA','BCA']
medium=['Hindi','English']
choice=['All of the Above','Advance Coding Skills','Spoken English','Personality Development']
sec =['A','B','C','D','E','F']
yr = ['/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div']
tec = ['/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div']
b=['/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div']
te=['/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div','/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div']

def gform():
    
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScgvsGpedKhe2jlZcaBRFbzmqjcIPlEnPww0RAs5KWzcbKkcw/viewform');
    time.sleep(0.1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(randomString(10) + " " + randomString(6))
    
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(randomString(10) + " " + randomString(6))
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(phone())
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(phone())
    #/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(randomString(10))
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(randomString(10))
    #driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(randomString(10)+"@gmail.com")
    #driver.find_element_by_xpath(random.choice(b)).click()
    driver.find_element_by_xpath(random.choice(te)).click()
    #driver.find_element_by_xpath(random.choice(tec)).click()
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span/span').click()
    
    
    
        
    '''
    driver.find_element_by_name('entry.421399345').send_keys(randomString(10) + " " + randomString(6)) #Student Name
    #print("Name")
    driver.find_element_by_name('entry.1361184693').send_keys(random.choice(branch)) # Branch
    #print("branch")
    driver.find_element_by_name('entry.1087895434').send_keys(random.randint(1,9)) #Semester
    #print("Sem")
    driver.find_element_by_name('entry.1691931581').send_keys(random.randint(1,60)) #Class RollNo
    #print("class")
    driver.find_element_by_name('entry.904339465').send_keys(random.randint(1,60))#School Name
    #print("School")
    #driver.find_element_by_name('entry.258562094').send_keys(random.choice(medium))#Medium
    driver.find_element_by_css_selector("div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl").click()
    #print("Medium")
    driver.find_element_by_name('entry.110891809').send_keys(random.randint(1,101))#Percentage
    #print("Percentage")
    #driver.find_element_by_name('entry.1436712148').send_keys(random.choice(choice))#Medium
    #print("Medium")
    driver.find_element_by_name('entry.1247693303').send_keys(randomString(30))#School Name  
    #print("School Name")
    test = driver.find_elements_by_css_selector("div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl")
    #print(test[6].click())
    #print(driver.find_element_by_css_selector("div.quantumWizTogglePaperradioOnRadio.exportInnerCircle").click())
    #driver.find_element_by_name('password').send_keys(gitpass)
    #driver.find_element_by_name('commit').click()
    time.sleep(0.1)
    driver.find_element_by_css_selector('div.quantumWizButtonEl.quantumWizButtonPaperbuttonEl.quantumWizButtonPaperbuttonFlat.quantumWizButtonPaperbuttonDark.quantumWizButtonPaperbutton2El2.freebirdFormviewerViewNavigationSubmitButton').click()
    '''
    
    
    #driver.find_element_by_css_selector('div.quantumWizButtonEl.quantumWizButtonPaperbuttonEl.quantumWizButtonPaperbuttonFlat.quantumWizButtonPaperbuttonDark.quantumWizButtonPaperbutton2El2.freebirdFormviewerViewNavigationSubmitButton.isUndragged').click()
    #driver.find_element_by_xpath("//div[@class='freebirdFormviewerViewNavigationButtons']/div").click()
    


for i in range(2000):
    gform()
    print(i)
    
    



  
