import psycopg2
#import gui
from datetime import datetime

#from build.gui import canvas2Refresh

conn = psycopg2.connect(database="ddgrckzh", user = "ddgrckzh", password = "KyJVEQaCDVV-8JeO1M96AEMAixTZVvde", host = "kesavan.db.elephantsql.com" )
cur = conn.cursor()

def errorHandling(e,conn):
        print(e)
        conn.rollback()


def createDbs():
#    cur.execute("drop TABLE stockInfo")
#    conn.commit()   

    cur.execute("CREATE TABLE IF NOT EXISTS skuInfo (id serial PRIMARY KEY, skuID INTEGER, sku_name varchar, weight FLOAT, volume FLOAT, price FLOAT)")
    conn.commit()   
    cur.execute("CREATE TABLE IF NOT EXISTS stockInfo (skuID varchar, stock0 INTEGER, delta_stock INTEGER, stock1 INTEGER, date TIMESTAMP DEFAULT NOW())")
    conn.commit()


def create_sku(skuID, sku_name, weight, volume, price):
    try:
        print("funciona")
        sql = "INSERT INTO skuinfo (skuID, sku_name, weight, volume, price) VALUES (%s, %s, %s, %s,%s)"
        val = (skuID, sku_name, weight, volume, price)
        cur.execute(sql,val)
        conn.commit()
        sql = f'INSERT INTO stockInfo (skuID, stock0, delta_stock, stock1, date) VALUES (%s, %s , %s , %s,NOW())'
        val = (skuID,"0","0","0")
        cur.execute(sql,val)
        conn.commit()

        
    except Exception as e: 
        errorHandling(e,conn)

def skuQuery(skuID):
        sql1 = "select stock1 from stockInfo where skuid='" + str(skuID) + "' order by date desc limit 1"
        cur.execute(str(sql1))
        stock0 = cur.fetchone()[0] 
        sql1 = "select sku_name from skuInfo where skuid='" + str(skuID) + "' group by 1 limit 1"
        cur.execute(str(sql1))
        skuName=cur.fetchone()[0]
        return skuName,stock0
       

def increase_stock(skuID, deltaStock,aux_val):
    try:
        sql1 = "select stock1 from stockInfo where skuid='" + str(skuID) + "' order by date desc limit 1"
        cur.execute(str(sql1))
        stock1 = int(cur.fetchone()[0])
        sql2 = 'INSERT INTO stockInfo (skuID, stock0, delta_stock, stock1, date) VALUES (%s, %s , %s , %s,NOW())'
        val = (skuID,str(stock1),str(aux_val*int(deltaStock)), (stock1+aux_val*int(deltaStock)))
        cur.execute(sql2,val)
        conn.commit()   

    except Exception as e: 
        errorHandling(e,conn)


def decrease_stock(skuID, stock):
    try:
        sql = ""
        val = (skuID, stock)
        cur.execute(sql,val)
        conn.commit()   
        cur.close()
        conn.close()

    except Exception as e: 
        errorHandling(e)