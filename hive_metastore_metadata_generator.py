import random

from pyhive import hive

_DATA_TYPES = ['TINYINT', 'SMALLINT', 'INT', 'BIGINT', 'FLOAT', 'DOUBLE', 'DECIMAL', 'TIMESTAMP', 'DATE',
               'STRING', 'BOOLEAN', 'BINARY', 'ARRAY<STRUCT< key:STRING, value:STRING>>',
               'ARRAY <STRING>', 'ARRAY <STRUCT <spouse: STRING, children: ARRAY <STRING>>>',
               'ARRAY<DOUBLE>', 'MAP<STRING,DOUBLE>', 'STRUCT < employer: STRING, id: BIGINT, address: STRING >',
               'UNIONTYPE<DOUBLE, STRING, ARRAY<string>, STRUCT<a:INT,b:string>>']

_COLUMN_NAMES = ['name', 'address', 'city', 'state', 'date_time', 'paragraph', 'randomdata', 'person', 'credit_card',
                 'size', 'reason', 'school', 'food', 'location', 'house', 'price', 'cpf', 'cnpj', 'passport',
                 'security_number', 'phone_number', 'bank_account_number', 'ip_address', 'stocks']

_DESCRIPTION_VALUES = ['This is a random generated column', 'Description for random generated column']

_TABLE_NAMES = ['school_info', 'personal_info', 'persons', 'employees', 'companies', 'store', 'home']

_DATABASE_NAMES = ['school_warehouse', 'company_warehouse', 'on_prem_warehouse', 'factory_warehouse',
                   'organization_warehouse']


def get_hive_conn(host, username, port=10000, schema="default"):
    return hive.connect(host=host, port=port, username=username, database=schema, auth=None)


def create_random_hive_data():
    conn = get_hive_conn('localhost', 'hive')

    cursor = conn.cursor()

    for x in range(random.randint(1, 5)):
        database_name, database_stmt = build_create_database_statement()
        cursor.execute(database_stmt)
        cursor.execute(build_use_database_statement(database_name))
        for y in range(random.randint(25, 50)):
            cursor.execute(build_create_table_statement())

    cursor.execute('show databases')
    databases = cursor.fetchall()
    print(databases)

    cursor.execute('show tables')
    tables = cursor.fetchall()
    print(tables)

    cursor.close()


def get_random_data_type():
    return random.choice(_DATA_TYPES)


def get_random_databases_name():
    return random.choice(_DATABASE_NAMES)


def get_random_column_name():
    return random.choice(_COLUMN_NAMES)


def get_random_column_description():
    return random.choice(_DESCRIPTION_VALUES)


def get_random_table_name():
    return random.choice(_TABLE_NAMES)


def build_create_database_statement():
    database_name = '{}{}'.format(get_random_databases_name(),
                                  str(random.randint(1, 100000)))
    database_stmt = 'CREATE DATABASE {} '.format(database_name)
    return database_name, database_stmt


def build_use_database_statement(database_name):
    return 'USE {} '.format(database_name)


def build_create_table_statement():
    table_stmt = 'CREATE TABLE {}{} ( '.format(
        get_random_table_name(),
        str(random.randint(1, 100000))
    )
    table_stmt = '{}{}{} {}'.format(
        table_stmt,
        get_random_column_name(),
        str(random.randint(1, 100000)),
        get_random_data_type()
    )
    for x in range(random.randint(1, 100)):
        table_stmt += ' , {}{}'.format(get_random_column_name(), str(random.randint(1, 100000))) + \
            '  {}'.format(get_random_data_type()) + \
            ' COMMENT "{}"'.format(get_random_column_description())

    table_stmt = '{} )'.format(table_stmt)
    return table_stmt


if __name__ == "__main__":
    create_random_hive_data()
