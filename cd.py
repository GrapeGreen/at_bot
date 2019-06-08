import requests_html, os
from selenium import webdriver

link = 'https://author.today/work/33438'

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
binary = webdriver.firefox.firefox_binary.FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')