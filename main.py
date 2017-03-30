# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import sys
import MySQLdb
import random
reload(sys)
sys.setdefaultencoding('utf8')
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="kamrica", use_unicode=True, charset='utf8')
cur = db.cursor()


z = 0
page=38078
linki = set()
#39623 med 38078
while page>38077 and page<39623:
    print page
    moj_url = 'http://www.dostop.si/KamricaOglas.aspx?ID='+str(page)
    r = urllib.urlopen(moj_url).read()
    soup = BeautifulSoup(r, "html.parser")
    if (soup.findAll('div', {'class': 'kontakt'})):
         linki.add('http://www.dostop.si/KamricaOglas.aspx?ID='+str(page))

         for itemText in (soup.findAll('div', {'class': 'kontakt'})):
            kontaktx = itemText.renderContents()
            print"{"+(kontaktx)+"}"

            insert_stmt = (
                        "INSERT INTO kontakti_kamrica(kontakt) "
                        "VALUES (%s)"
                    )
            data = (kontaktx)
            cur.execute(insert_stmt, data)
         z+=1
    page += 1
    print "-------------------------------------------------------------------------------------------"
