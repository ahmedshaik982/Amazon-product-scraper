
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
import time
cService = webdriver.ChromeService(executable_path='C:/Users/HP/Downloads/scraping/chromedriver.exe')
driver = webdriver.Chrome(service = cService)
url = 'https://www.amazon.in/s?i=watches&bbn=2563505031&rh=n%3A2563505031%2Cp_n_material_browse%3A1480914031%7C1480915031%2Cp_n_feature_two_browse-bin%3A1480926031&s=watches&dc&ds=v1%3AeM2eLIa8B4TSuXM1VBHFK%2FKFsjfH1pec8nVX8ihoC%2FA&pf_rd_i=2563505031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=bd9f5519-fc02-4b06-bccd-9833eb13067b&pf_rd_r=W99PTGA670NTV07HFRY6&pf_rd_s=merchandised-search-26&qid=1714473933&rnid=1480889031&ref=sr_nr_p_n_material_browse_8'
driver.get(url)
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('xpath', '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]')))
final = []
k = 1
for j in range(45): 
    for i in range(47):
        print(k)
        lst = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(1 + k)+ ']')
        k = k + 1
        child_element = lst.find_element(By.XPATH, './*')
        child_2 = child_element.find_element(By.XPATH, './*')
        child_3 = child_2.find_element(By.XPATH, './*')
        child_4 = child_3.find_element(By.XPATH, './*')
        child_5 = child_4.find_element(By.XPATH, './*')
        child_6 = child_5.find_elements(By.XPATH, './*')
        all_elem = child_6[-1].find_elements(By.XPATH, './*')
        res = []
        try:
            title = all_elem[0].find_elements(By.XPATH, './*')[-1].text
            res.append(title)
        except:
            res.append('NA')
            
        try:
            price = all_elem[2].find_elements(By.XPATH, './*')[0].text.split('\n')[0]
            res.append(price)
        except:
            res.append('NA')
            
        try:
            r = all_elem[1].find_element(By.XPATH, './*')
            rating = r.find_elements(By.XPATH, './*')[0].get_attribute('aria-label')
            res.append(rating)
        except:
            res.append('NA')
        
        try:
            num = all_elem[1].find_element(By.XPATH, './*').text
            res.append(num)
        except:
            res.append('NA')
        final.append(res)
    k = 1
    try:
        if j != 44:
            nxt = driver.find_element(By.LINK_TEXT, 'Next')
            nxt.click()
            time.sleep(2)
        if j == 44:
            print('its over')
    except:
        print('its over')
    
dataframe = pd.DataFrame(final, columns=['title', 'price', 'rating', 'Number of ratings'])

len(final)









