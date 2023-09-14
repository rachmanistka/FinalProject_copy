from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser,link)
    login_page=LoginPage(browser,browser.current_url)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page.should_be_login_page()