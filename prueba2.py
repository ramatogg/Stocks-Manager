
import psycopg2

conn = psycopg2.connect(database="ddgrckzh", user = "ddgrckzh", password = "KyJVEQaCDVV-8JeO1M96AEMAixTZVvde", host = "kesavan.db.elephantsql.com" )
cur = conn.cursor()

try:
    cur.execute("CREATE TABLE skuInfo (id serial PRIMARY KEY, skuID INTEGER, sku_name varchar, weight FLOAT, volume FLOAT, price FLOAT)")

except Exception as e: 
    print(e)
    conn.rollback()

try:
    sql = "INSERT INTO skuinfo (skuID, sku_name, weight, volume, price) VALUES (%s, %s, %s, %s,%s)"
    val = (10315175,"lampa11ra de dia",1300,2,1300)
    cur.execute(sql,val)
    conn.commit()   
    cur.close()
    
except Exception as e: 
    print(e)
    conn.rollback()

#cur.execute("SELECT * FROM test")
#movimientos asi: sku id, stock0, ingreso/egreso,  stock1
#, created_AT DATE DEFAULT CURRENT_DATE
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

conn.close()

"""
drop="DROP table skuinfo"
cur.execute(drop)
"""

