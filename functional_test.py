from selenium import webdriver

browser = webdrver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
