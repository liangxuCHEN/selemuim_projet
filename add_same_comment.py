#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os
import sys
from meminformation import meminfo

def restart_program():  
    """Restarts the current program. 
    Note: this function does not return. Any cleanup action (like 
    saving data) must be done before calling this function."""  
    python = sys.executable  
    os.execl(python, python, * sys.argv)

def init():
    dirver = webdriver.Firefox()
    return dirver

def login(dirver, name, password):
    dirver.get("http://login.qyer.com/login.php")
    time.sleep(1)
    dirver.find_element_by_name('mail_input').send_keys(name)
    dirver.find_element_by_name('password').send_keys(password)
    dirver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/input').click()

#dirver.get('http://bbs.qyer.com/thread-785994-1.html')
def comment(dirver, url,  text):
    dirver.get(url)
    time.sleep(4)
    dirver.find_element_by_id('topicReplyDefault').click()
    dirver.execute_script("""
    var f = document.getElementById("topicReplyEditor").getElementsByTagName('iframe')[0];
    var doc = f.contentWindow.document;
    doc.body.innerHTML ="<p>欢迎咨询预订！</p>";
    """)
    button = dirver.find_element_by_xpath("//div[@id='topicReplyEditor']//input")
    button.click()

if __name__ == "__main__":
    name = []
    password = []
    url = []
    
    name.append(u'xxx')
    password.append(u'xx')
    url.append(u'x')
    name.append(u'x')
    password.append(u'xxx')
    url.append(u'xxx')

    text = u'欢迎咨询预订！或者直接拨打电话：40084-50085 !'
    i = 0
    while True:
        try:
            dirver = init()
            time.sleep(2)
            login(dirver, name[i], password[i])
            time.sleep(6)
            comment(dirver, url[i], text[i])
            dirver.close()
        except:
            #answer = raw_input("Do you want to restart this program ? ")
            #if answer.strip() in "y Y yes Yes YES".split():
            print 'the program has some problems, and it will restart after 1h'
            mem_free = meminfo('MemFree')
            print("Free memory:{0}".format(mem_free))
            time.sleep(3600)
            restart_program()
        
        time.sleep(5400)
        i = (1+i) % 2

