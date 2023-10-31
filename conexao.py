#conexão com banco de dados

import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        dbconfig = {
            'host':'127.0.0.1',
            'user':'senai_pp',
            'password':'1234',
            'database':'escola',
        }

        con = mysql.connector.connect(**dbconfig)
        return con
    except(Exception, Error) as error:
        print('Não conectou! ' +str(error))

def read(con):
    cursor = con.cursor()

    query = '''SELECT * FROM estudante;'''

    try:
            cursor.execute(query)

            print('\n\t\t\t ** SENAI - LISTA DE CHAMADA ** ')
            print('\t -- RA -- \t\t ---------- Nome ------------')
            for campo in cursor.fetchall():
                print(f'\t{campo[0]} \t \t\t {campo[1]}')
                # print(f'\tRA: {campo[0]} - Nome: {campo[1]}')

    except(Exception, Error) as error:
        print('Conectou mas não funcionou! ' +str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print('\n\n Conexão fechada!\n')

# Teste
read(conectar())