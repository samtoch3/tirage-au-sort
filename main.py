# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 01:44:17 2022

@author: Samson N.

-- Controler un navigateur avec python
-- doc : https://selenium-python.readthedocs.io/index.html
-- doc : https://pypi.org/project/selenium/

module nécessaire :
    pip install selenium
    
"""


from selenium import webdriver


# Creer un variable pour declencher le driver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.kubii.fr/')

# recuperer dans la barre de recherche
search_bar = driver.find_element_by_id('search_query_top')
search_bar.send_keys('Arduino')

# recuperer le bouton pour lancer la recherche
search_btn = driver.find_element_by_id('searchbox')
search_btn.click()

# recuperer tous les noms des produits
all_products = driver.find_elements_by_class_name('product-name')

# parcourir la liste des produits
for title in all_products:
    print(title.text)


driver.quit()

