import urllib
from bs4 import BeautifulSoup
from mechanize import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

chromedriver = "C:/Users/Diego Campos/chromedriver_win32/chromedriver.exe"
url = "http://apps.contraloria.gob.pe/ciudadano/wfm_obras_buscador.aspx"
driver = webdriver.Chrome(chromedriver)

driver.get(url)
#Seleccionar Departamento
departamento = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ddlDepartamento"]""")))
driver.find_element_by_xpath("""//*[@id="ddlDepartamento"]/option[15]""").click()
#Seleccionar Provincia
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ddlProvincia"]""")))
driver.find_element_by_xpath("""//*[@id="ddlProvincia"]/option[2]""").click()
#Seleccionar Distrito
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ddlDistrito"]""")))
driver.find_element_by_xpath("""//*[@id="ddlDistrito"]/option[2]""").click()
#Resolver Captcha

#submit