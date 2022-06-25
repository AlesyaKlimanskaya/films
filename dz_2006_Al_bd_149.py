# 1. Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, name TEXT, release_year INT, genre TEXT.
# 2. Создать функции: 1) Добавить фильм (заполнение делать с клавиатуры);
# 2) Получение данных обо всех фильмах; 3) Получение данныхоб одном фильме по id. 0. Выход.
# 3. Функции вызывать в цикле, чтобы у пользователя был выбор

import sqlite3
conn = sqlite3.connect("films.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
movie_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, release_year INT, genre TEXT)''')
conn.commit()

def insert_film():
    name = input('Введите название фильма: ')
    release_year = int(input('Введите год выпуска фильма: '))
    genre = input('Введите жанр фильма: ')
    try:
        cursor.execute('''SELECT name FROM movies WHERE name = ?''', [name])
        if cursor.fetchone() is None:
            values = [name, release_year, genre]
            cursor.executemany('''INSERT INTO movies(name, release_year, genre) VALUES (?, ?, ?)''', (values,))
            conn.commit()
        else:
            print('Данный фильм уже есть в фильмотеке!')
            insert_film()

    except sqlite3.Error as e:
        print('Error', e)
    finally:
        conn.close()

def select_film():
    cursor.execute('''SELECT*FROM movies''')
    k = cursor.fetchall()
    for i in k:
        j = ','.join([str(j) for j in i])
        print(j)

def id_film():
    try:
        h = int(input('Чтобы получить данные о фильме введите его id: '))
        cursor.execute('''SELECT*FROM movies WHERE movie_id=?''', (h,))
        s = cursor.fetchall()
        print(s)

    except ValueError:
        print('Вы ввели не число!')
        id_film()

while True:
    print(''' Добро пожаловать в нашу фильмотеку!!!
    1) Добавте фильм.
    2) Желаете получить данные о всех фильмах?
    3) Желаете получить данные по выбранному фильму?
    0) Выход из фильмотеки.
    ''')
    f = int(input('Чтобы сделать выбор введите число (0-3): '))
    if f == 0:
        break
    elif f == 1:
        insert_film()
        d = input('''Чтобы продолжить ввод данных нажмите(*)
Чтобы закончить ввод данных нажмите (-): ''')
        if d == '*':
            insert_film()
        elif d == '-':
            continue
    elif f == 2:
        select_film()
    elif f == 3:
        id_film()
    elif f > 3:
        print('Вы ввели не верное число!')
        continue


