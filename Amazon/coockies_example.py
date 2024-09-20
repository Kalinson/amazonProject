import time
import os
import pickle
from os import getcwd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.amazon.com/TriggerPoint-Channel-Exercise-Massage-Recovery/dp/B091BJT2QP/ref=pd_ci_mcx_mh_pe_im_d1_cau_p_0?pd_rd_i=B091BJT2QP&pd_rd_w=irjEa&content-id=amzn1.sym.d0595222-359f-4c32-b2c9-3db3ca85b802&pf_rd_p=d0595222-359f-4c32-b2c9-3db3ca85b802&pf_rd_r=BYX4JGSQ2Z8RZ55ZDMF0&pd_rd_wg=H8ZCy&pd_rd_r=cb4115d0-5552-4c93-af0e-080d1e550cf9")

ADD = ("xpath", "//input[@id = 'add-to-cart-button']")
wait.until(EC.presence_of_element_located(ADD)).click()

time.sleep(3)

NO_THANKS = ("xpath", "//input [@aria-labelledby='attachSiNoCoverage-announce']")
wait.until(EC.presence_of_element_located(NO_THANKS)).click()

time.sleep(3)

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()

driver.refresh()

LOAD_COOKIES = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))

driver.refresh()

time.sleep(5)