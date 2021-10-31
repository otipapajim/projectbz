#!C:\Users\Sigma\AppData\Local\Programs\Python\Python39\python.exe
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
import mysql.connector
import traceback
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="r6eAbana@wasak1",
  database="sas"
)

#TODO
#Make last page determination automatic
#Find a better way to do this

f = open("currdata.txt", "r")
sku = f.read()

prepareddrop ="DROP TABLE IF EXISTS " +sku
preparedcreate ="CREATE TABLE " +sku+" (number INT(4) NOT NULL AUTO_INCREMENT, review VARCHAR(500)NOT NULL,PRIMARY KEY (number))"
mycursor = mydb.cursor()
mycursor.execute(""+prepareddrop)
mycursor.execute(""+preparedcreate)


pages = np.arange(0, 12, 1)



for page in pages:

    url = "https://www.jumia.co.ke/catalog/productratingsreviews/sku/"+sku+"/?page="+str(page)
    try:
        page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
        infile=urllib.request.urlopen(page).read()
        data = infile.decode('utf-8')   
        soup = BeautifulSoup(data, 'html.parser')

        content = soup.find('div', {"class": "cola -phm -df -d-co"})

        article = ''
        for i in content.findAll('p'):           
            article = article + '' + i.text +'\n'

            
        listifyarticle = (article.splitlines())
        #print(listifyarticle)
        for d in listifyarticle:
            preparedinsert = "INSERT INTO "+sku+"(review) VALUES (%r)" % (d,)
            #print(preparedinsert)            
            mycursor.execute(""+preparedinsert)
            mydb.commit()

        #with open('scraped_text.txt', 'w') as file:
         #   file.write(article)
            
    
    except Exception:
        print(traceback.format_exc())


