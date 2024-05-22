"""
Task olaraq sadece bu proyekti dahada tekminlesdirmeyinizi 
elave bir cox sql methodlari istifade etmeyinizi isteyirem. 
Ayri bir movzuya uygun db yaradin, 
ferqli funksiyalar ile sql isdedin.

"""
#CTRL + R => for refreshing the DB on SQLITE
#DB ile connectio yaratma
import sqlite3
connection = sqlite3.connect("neneminfermasi.sqlite")
cursor = connection.cursor()


#Cedvel yaratma
def create__table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Animals(ID INT, Name TEXT, Count INT, Price INT, Origin_country TEXT)")
    connection.commit()
    
# create__table()

#Cedvele data elave etme 
def add__table():
    cursor.execute("INSERT INTO Animals VALUES (1, 'Capybara', 15, 230, 'Brazil')")
    connection.commit()
    
# add__table()

#Cedvele elave olunan datani dinamiklesdirmek
def dynamic_add_table(ID,Name,Count,Price,Origin_country):
    cursor.execute("INSERT INTO Animals VALUES(?,?,?,?,?)", (ID,Name,Count,Price,Origin_country))
    # connection.commit()

# ID = int(input("ID-ni daxil edin: "))
# Name = input("Heyvanin adini daxil edin: ")
# Count = int(input("Heyvanin sayini daxil edin: "))
# Price = int(input("Zehmet olmasi 1 heyvan ucun qiymet daxil edin: "))
# Origin_country = input("Getirildiyi olkeni daxil edin: ")

# dynamic_add_table(ID,Name,Count,Price, Origin_country)


#Datani cekib gosterme
def show__data():
    cursor.execute("SELECT * FROM ANIMALS")
    data = cursor.fetchall()
    for row in data:
        print(row)
        
# show__data()


#Axtarialacaq acar soze gore datani gosterme
def dynamic_show_data():
    cursor.execute("SELECT COUNT, ORIGIN_COUNTRY AS OC FROM ANIMALS WHERE Name = ?", (Name, ))
    data = cursor.fetchall()
    for row in data:
        print (f"Hemin heyvanin sayi ve getirildiyi olke: {' '.join(map(str, row))}")
        
# Name = input("Maraqlandiginiz heyvan adini bize bexs edin: ")
# dynamic_show_data()

#Axtarialacaq acar sozden basqa diger datalari gostere biler sadece fetchmany ile limitledim bu sayi
def dynamic_show_data2():
    cursor.execute("SELECT * FROM ANIMALS WHERE NOT Name = ?", (Name, ))
    data = cursor.fetchmany(5)
    for row in data:
       print(row)
        
# Name = input("Maraqlanmadiginiz heyvan adini bize bexs edin: ")

# dynamic_show_data2()


#Xanalardaki datani yenileme
def update__name(old_name, new_name):
    cursor.execute("UPDATE ANIMALS SET NAME  = ? where name = ?", (new_name, old_name))
    connection.commit()
    
# old_name = input("Adini deyismeyi bexs etdiyiniz heyvanin adini qeyd etme zamani: ")
# new_name = input("Yeni ad: ")

    
# update__name(old_name,new_name)


def update__count(old_count, new_count):
    cursor.execute("UPDATE ANIMALS SET COUNT = ? WHERE COUNT = ?",(new_count, old_count))
    connection.commit()
    
# update__count(56,76)

#Deleting data
def delete__data(Name):
    cursor.execute("DELETE FROM ANIMALS WHERE NAME = ?",(Name, ))
    connection.commit()

# delete__data("Coala")

#Showing distinc data
def unique__data():
    cursor.execute("SELECT DISTINCT(COUNT) FROM ANIMALS")
    data = cursor.fetchall()
    for row in data:
        print(row)

# unique__data()

#Average value
def avg__price():
    cursor.execute("SELECT AVG(PRICE * COUNT)  FROM ANIMALS")
    connection.commit()
    data = cursor.fetchall()
    for row in data:
        print(row)
    
# avg__price()

#Showing min and max
def min__max__price():
    cursor.execute("SELECT MIN(PRICE) FROM ANIMALS")
    min_price = cursor.fetchone()[0] #index is needed for tuple
    cursor.execute("SELECT MAX(PRICE) FROM ANIMALS")
    max_price = cursor.fetchone()[0]
    print(f"Minimum price: {min_price} and maximum price: {max_price}")

# min__max__price()


#Araliga gore qiymet cixarma
def between__price(first_number, last_number):
    cursor.execute("SELECT PRICE FROM ANIMALS WHERE PRICE BETWEEN ? AND  ?", (first_number, last_number))
    prices = cursor.fetchall()
    print('\n'.join(map(str, prices)))
    connection.commit()
    
# first_number = int(input("Arealigin ilk ededini qeyd edin: "))
# last_number = int(input("Araligin ikinci ededini qeyd edin: "))

# between__price(first_number,last_number)


#CASE ...  THEN
def case__then():
    cursor.execute("SELECT COUNT, NAME, CASE WHEN COUNT > 32 THEN 'The COUNT is greater than 32' WHEN COUNT = 32 THEN 'The COUNT is 32' ELSE 'The COUNT is under 32' END AS COUNTText FROM ANIMALS")
    data = cursor.fetchall()
    for row in data:
        print(row)
        
case__then()

cursor.close()
connection.close()
    
