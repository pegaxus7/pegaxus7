
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


web = webdriver.Edge()
web.get('')

time.sleep(3)

Nama = ""
Na   = web.find_element(By.XPATH, '')
Na.send_keys(Nama)

PilihanKelas = web.find_element(By.XPATH, '')
PilihanKelas.click()

Nim = ""
Ni  = web.find_element(By.XPATH, '')
Ni .send_keys(Nim)

Kirim = web.find_element(By.XPATH, '')
Kirim.click()

get_confirmation_div_text = web.find_element(By.CSS_SELECTOR,'.vHW8K')
print (get_confirmation_div_text.text)
if((get_confirmation_div_text)== "jawaban anda telah direkam."):
    print("Berhasil Mengirim")
else:
    print("Tidak Berhasil Mengirim")

