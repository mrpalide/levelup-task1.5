from random import randint

import psycopg2

con = psycopg2.connect(
    database="task1o5", user="postgres", password="root", host="localhost", port="5432"
)
print("DB opened successfully")

cur = con.cursor()
customer_table: str = "CREATE TABLE CUSTOMER (ID SERIAL PRIMARY KEY  NOT NULL, NAME TEXT NOT NULL, PREMIUMSOURCES TEXT);"
product_table: str = "CREATE TABLE PRODUCT (ID SERIAL PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, CUSTOMER_ID INT REFERENCES CUSTOMER (ID) ON DELETE RESTRICT NOT NULL);"
source_table: str = "CREATE TABLE SOURCE (ID SERIAL PRIMARY KEY  NOT NULL, NAME TEXT NOT NULL, TYPE INT NOT NULL);"
offer_table: str = "CREATE TABLE OFFER (ID SERIAL PRIMARY KEY NOT NULL, PRODUCT_ID INT REFERENCES PRODUCT (ID) ON DELETE RESTRICT NOT NULL, SOURCE_ID INT REFERENCES SOURCE (ID) ON DELETE RESTRICT NOT NULL, ORDER_NUM INT);"

cur.execute(customer_table)
cur.execute(product_table)
cur.execute(source_table)
cur.execute(offer_table)
print("Table create successfully")

customer_range: int = 10
product_count: int = 1000
source_free: int = 5
source_premium: int = 3
offer_count: int = 20000

for i in range(customer_range):
    cur.execute(
        f"INSERT INTO CUSTOMER (ID,NAME,PREMIUMSOURCES) VALUES (DEFAULT,'customer_{i+1}', '')"
    )

for i in range(source_free):
    cur.execute(
        f"INSERT INTO SOURCE (ID,NAME,TYPE) VALUES (DEFAULT,'source_free_{i+1}', 0)"
    )

for i in range(source_premium):
    cur.execute(
        f"INSERT INTO SOURCE (ID,NAME,TYPE) VALUES (DEFAULT,'source_premium_{i+1}', 1)"
    )

for i in range(product_count):
    cur.execute(
        f"INSERT INTO PRODUCT (ID,NAME,CUSTOMER_ID) VALUES (DEFAULT, 'product_{i+1}', {randint(1,customer_range)})"
    )

for i in range(offer_count):
    cur.execute(
        f"INSERT INTO OFFER (ID, PRODUCT_ID, SOURCE_ID, ORDER_NUM) VALUES (DEFAULT, {randint(1,product_count)}, {randint(1,source_free+source_premium)},NULL)"
    )


con.commit()
con.close()
