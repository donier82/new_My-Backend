"БД - База Данных"
"СУБД - Система Управления Базой Данных"

"CRUD - Create, Read, Update, Delete"


import sqlite3

connect = sqlite3.connect("Back_19_1.db")
cursor = connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            hobby TEXT DEFAULT NULL,
            phone_number INT NOT NULL DEFAULT 996,
            birth_date DATE,
            mark DOUBLE (5, 2) DEFAULT 0.0,
            is_mentor BOOLEAN DEFAULT False    
               )""")


def add_student():
    user_full_name = input("Введите имя: ")
    user_hobby = input("Введите хобби: ")
    user_phone_number = int(input("Введите номер телефона: "))
    user_birth_date = input("Введите дату рождения: ")

    cursor.execute(f"SELECT phone_number FROM students WHERE phone_number = {user_phone_number}")
    student = cursor.fetchone()

    if student:
        print("Вас уже добавили в табель")
    else:
        cursor.execute(f"""INSERT INTO students
                    (full_name, hobby, phone_number, birth_date)
                    VALUES ('{user_full_name}', '{user_hobby}', {user_phone_number}, '{user_birth_date}')""")
    
    # cursor.execute("""INSERT INTO students
    #                (full_name, hobby, phone_number, birth_date)
    #                VALUES ('?', '?', ?, '?')""", user_full_name, user_hobby, user_phone_number, user_birth_date)
    
    connect.commit() 

# add_student()

def all_student():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

# all_student()

def delete_student():
    user_id = int(input("Введите id студента: "))
    cursor.execute(f"SELECT id, full_name FROM students WHERE id = {user_id}")
    student = cursor.fetchone()

    if student:        
        cursor.execute(f"DELETE FROM students WHERE id = {user_id}")
        connect.commit()
        print(f"Студент {student} удален")
    else:
        print("Такого студента нет в табели")

# delete_student()

def update_student():
    user_id = int(input("Введите id студента: "))
    user_full_name = input("Введите имя: ")
    user_hobby = input("Введите хобби: ")
    user_phone_number = int(input("Введите номер телефона: "))
    user_birth_date = input("Введите дату рождения: ")
    user_mark = float(input("Введите новую оценку: "))
    user_mentor = bool(input("Стал студент ментором?: "))

    cursor.execute("""UPDATE students SET 
                   full_name = ?, hobby = ?, phone_number = ?, 
                   birth_date = ?, mark = ?, is_mentor = ? WHERE id = ?""", (user_full_name, user_hobby, user_phone_number, user_birth_date, user_mark, user_mentor, user_id))
    connect.commit()

# update_student()

def update_student_mark():
    user_id = int(input("Введите id студента: "))
    user_mark = float(input("Введите новую оценку: "))

    cursor.execute("""UPDATE students SET 
                mark = ? + ? WHERE id = ?""", (user_mark, user_mark, user_id))
    connect.commit()

update_student_mark()