import pymysql.cursors

connection = pymysql.connect(
    host = 'localhost',
    user = 'blockchain_program_admin',
    password = 'blockchain305',
    database = 'blockchain_program',
    cursorclass = pymysql.cursors.DictCursor
)

with connection:
    # with connection.cursor() as cursor:
    #     sql = 'INSERT INTO users (name, user_name, password) VALUES (%s, %s, %s);'
    #     cursor.execute(sql, ('name1', 'user1', 'password1'))

    connection.commit()

    with connection.cursor() as cursor:
        sql = 'select * from users WHERE user_name = %s;'
        cursor.execute(sql, ('user1'))
        result = cursor.fetchone()
        print(result)