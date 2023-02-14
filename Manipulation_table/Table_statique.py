import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
#recuperation le nombres de lignes et colonnes d'une table
nombres_lignes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(nombres_lignes))
nombres_colonnes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(nombres_colonnes))
#recuperer la valeur d'une cellue da la table
valeur_celle=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(valeur_celle.text)
#recuperer toutes les donnees du tableau
nb_lignes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
nb_colonnes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
valeur_head=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
"""for h in range(1,len(valeur_head)+1):
    data_head=driver.find_element(By.XPATH,"//table[@name='BookTable']//th["+str(h)+"]").text
    print(data_head)"""
time.sleep(3)
"""for r in range(2,nb_lignes+1):
    for c in range(1,nb_colonnes+1):
        val_cel=val_cell=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        #val_cel = driver.find_element(By.XPATH,"//tabel[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(val_cel,end='  ')
    print()"""
for r in range (2,nb_lignes+1):
    auteur=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if auteur == "Amit":
        prix=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        nom_livre=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        print(auteur,"***********",nom_livre,"***********",prix)

driver.close()