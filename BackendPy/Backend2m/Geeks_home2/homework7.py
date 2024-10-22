# ДЗ №7

# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
import sqlite3
connect=sqlite3.connect('hw.db')
cursor=connect.cursor()

# 2. В БД создать таблицу products

# 3. В таблицу добавить поле id - первичный ключ, тип данных числовой и добавить автоикрементацию .
# 4. Добавить поле product_title (название продукта) текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым.
# 5. Добавить поле price (цена продукта) не целочисленного (float) типа данных размером 6 цифр из которых 3 цифры поле плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity (количество продукта) целочисленного (int) типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_title VARCHAR (50) NOT NULL,
               price DOUBLE(3,3) DEFAULT 0.0,
               quantity INT NOT NULL DEFAULT 0               
               )''')

# 7. Создать функцию для добавления продуктов в БД.
# 8. Создать функцию для просмотра название продуктов и цен
def add_product():
    user_product_title=input('введите название продукта: ')
    user_price=float(input('введите цена товара: '))
    user_quantity=int(input('введите количество товара: '))

    cursor.execute(f"SELECT product_title FROM products WHERE product_title='{user_product_title}'")
    product=cursor.fetchone()

    if product:
        print(f'товар {user_product_title} существует')
    else:
        cursor.execute(f"""INSERT INTO  products
                       (product_title,price,quantity)
                       VALUES 
                       ('{user_product_title}',{user_price},{user_quantity})""")
                        # или такой более безопасный вариант 
                        # VALUES
                        # ('?',?,?)""",user_product_title,user_price,user_quantity)

connect.commit()        # это для закрепление (зафиксирует введенные текст)

add_product()           # запускает функции add_product

def all_product():
    cursor.execute('SELECT * FROM products')    # можно заменить на product_title,price,quatity
    products=cursor.fetchall()
    print(products)

all_product()           #   вызывает функцию    all_product


        