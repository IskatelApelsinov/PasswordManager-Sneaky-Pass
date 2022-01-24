##### везде сделать коммит!!!!!!!

import psycopg2
from psycopg2 import Error
class Svyaz_s_bd(object):
    def __init__(self):
        #mchs_project
        super(Svyaz_s_bd, self).__init__()
        self.log = ''
        self.pas = ''
        self.address = '127.0.0.1'   #### local host
        self.port = '5432'   ##### local port
        self.database = 'manager'     ##### name default database
        self.connection = ''  #### connection объект работы с бд
    # Подключение к существующей базе данных
    def connect(self, login, password, address, port, database):
        try:
            connection = psycopg2.connect(user=login,
                                          password=password,
                                          host=address,
                                          port=port,
                                          database=database)
            #"127.0.0.1" "5432"
            # Курсор для выполнения операций с базой данных
            self.cursor = connection.cursor()
            # Распечатать сведения о PostgreSQL
            #print("Информация о сервере PostgreSQL")
            #print(connection.get_dsn_parameters(), "\n")
            # Выполнение SQL-запроса
            self.cursor.execute("SELECT version();")
            # Получить результат
            record = self.cursor.fetchone()
            #print("Вы подключены к - ", record, "\n")
            self.connection = connection
            return connection
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        # finally:
        #     if connection:
        #         cursor.close()
        #         connection.close()
        #     print("Соединение с PostgreSQL закрыто")
    def local_connect(self, login, password):
        try:
            connection = psycopg2.connect(user=login,
                                          password=password,
                                          host=self.address,
                                          port=self.port,
                                          database=self.database)
            #"127.0.0.1" "5432"
            # Курсор для выполнения операций с базой данных
            self.cursor = connection.cursor()
            # Распечатать сведения о PostgreSQL
            #print("Информация о сервере PostgreSQL")
            #print(connection.get_dsn_parameters(), "\n")
            # Выполнение SQL-запроса
            self.cursor.execute("SELECT version();")
            # Получить результат
            record = self.cursor.fetchone()
            #print("Вы подключены к - ", record, "\n")
            self.connection = connection
            return connection
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        # finally:
        #     if connection:
        #         cursor.close()
        #         connection.close()
        #     print("Соединение с PostgreSQL закрыто")
    def close_connect(self):
        if self.connection:
            self.connection.cursor().close()
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")

    def auto_conn(self):
        #self.local_connect('user_71749801', 'parolchela')
        self.local_connect('postgres', '123123')

    def login_user(self, login, pswd):
    #self.cursor.execute('call full_delete_rus(%s)', (number))
        try:
            #print(login, pswd)
            self.cursor.execute('select select_id(%s, %s)', (login, pswd))
            result = self.cursor.fetchone()
            if result == None:
                return False
            else:
                return result[0]

        except (Exception, Error) as error:
            print("Ошибка при работе с БД", error)

    def reg_polz(self, login, passwd, email):
        try:
            #print(login, pswd)
            self.cursor.execute('call create_user(%s, %s, %s)', (login, passwd, email))
            #result = self.cursor.fetchone()
            #print(result, '123')
            self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def show_zap(self, id):
        try:
            #print(login, pswd)
            #self.cursor.execute('select pokaz(%s)', (id))
            zapros = 'select * from pokaz(' + str(id) + ');'
            self.cursor.execute(zapros)
            result = self.cursor.fetchall()
            #print(result)
            return result
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def add_zap(self, id, nazwanie, login, passwd):
        try:
            #print(login, pswd)
            self.cursor.execute('call add_servis(%s, %s, %s, %s)', (id, nazwanie, login, passwd))
            #zapros = 'select pokaz(' + str(id) + ');'
            #self.cursor.execute(zapros)
            #result = self.cursor.fetchall()
            #print(result)
            self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def del_zap(self, id):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            zapros = ('call delete_servis(' + id + ')')
            #print(zapros)
            self.cursor.execute(zapros)
            self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def edit_log_zap(self, id_chel, id_zap, new_login):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)

            self.cursor.execute('call edit_login_servis(%s, %s, %s)', (id_chel, id_zap, new_login ))
            self.commit_bd()
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            self.rollback_bd()
    def edit_pass_zap(self, id_chel, id_zap, new_pass):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)

            self.cursor.execute('call edit_parol_servis(%s, %s, %s)', (id_chel, id_zap, new_pass ))
            self.commit_bd()
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            self.rollback_bd()

    def take_info(self, id):
        try:
            zapros = ('select * from wywod_po_id(' + str(id) + ')')
            #print(zapros)
            self.cursor.execute('select * from wywod_po_id(%s)', str(id))
            info = self.cursor.fetchall()
            return info
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def change_pass_user(self, id_polz, login, old_pass, new_pass):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)

            self.cursor.execute('select edit_parol_sneakpass(%s, %s, %s, %s)', (id_polz, login, old_pass, new_pass ))
            self.commit_bd()
            return self.cursor.fetchone()
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            self.rollback_bd()

    def rollback_bd(self):
        self.connection.rollback()

    def commit_bd(self):
        self.connection.commit()

    def proverka_login(self, login):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)

            self.cursor.execute('select proverka_login(%s)', (login, ))
            otv = self.cursor.fetchone()
            #print(login, otv)
            return otv[0]
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def proverka_email(self, email):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)

            self.cursor.execute('select proverka_po4ta(%s)', (email, ))

            return self.cursor.fetchone()[0]
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def start_paswd(self, id_polz, salt):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)
            #print(id_polz, salt)
            self.cursor.execute('call hash_add(%s, %s)', (id_polz, salt))
            self.commit_bd()
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error, 'nachalo')

    def konec_raboty(self):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)
            self.cursor.execute('call hash_delete()')
            self.commit_bd()
            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error, 'konec')

    def deshifrator(self, id_polz, id_servis):
        try:
            #print('del', id)
            #zapros = ('call delete_servis(%s)', str(id))
            #zapros = ('call delete_servis(' + id + ')')
            #print(zapros)
            self.cursor.execute('select * from deshifrator(%s, %s)', (id_polz, id_servis))
            rez = self.cursor.fetchall()
            rez = rez[0]
            rez = rez[0]
            #print(rez)
            return rez

            #self.connection.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error, 'konec')