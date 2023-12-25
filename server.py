import socket
import sqlite3
import os
from threading import Thread


def connect_client():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    connection, address = server_socket.accept()  # accept new connection
    return connection, address


def send_message(connection, message):
    connection.send(message.encode('utf-8'))


def receive_response(connection):
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = connection.recv(1024).decode('utf-8')
    return data


def connect_database(filename):
    create = not os.path.exists(filename)
    database = sqlite3.connect(filename, check_same_thread=False)
    if create:
        cursor = database.cursor()
        cursor.execute("""CREATE TABLE User(
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
                        username TEXT NOT NULL, 
                        password TEXT NOT NULL,
                        user_type TEXT NOT NULL );""")

        cursor.execute("""CREATE TABLE Tournament(
                        team_name TEXT NOT NULL, 
                        race_type TEXT NOT NULL,
                        score TEXT,
                        date TEXT NOT NULL,        
                        time TEXT NOT NULL, 
                        event TEXT,
                        status TEXT NOT NULL);""")
        database.commit()
        initialization_data(database)
        return database
    else:
        return database


def initialization_data(database):
    cursor = database.cursor()
    insert_data = "INSERT INTO Tournament VALUES (?, ?, ?, ?, ?, ?, ?)"
    data = [('Qatar vs Ecuador', 'Group A', '0 · 2', '21 Nov 2022', '00:00', '', 'FT'),
            ('England vs Iran', 'Group B', '6 · 2', '21 Nov 2022', '21:00', '', 'FT'),
            ('Senegal vs Netherlands', 'Group A', '0 · 2', '22 Nov 2022', '00:00', '', 'FT'),
            ('United States vs Wales', 'Group B', '1 · 1', '22 Nov 2022', '03:00', '', 'FT'),
            ('Argentina vs Saudi Arabia', 'Group C', '1 · 2', '22 Nov 2022', '18:00', '', 'FT'),
            ('Denmark vs Tunisia', 'Group D', '0 · 0', '22 Nov 2022', '21:00', '', 'FT'),
            ('Mexico vs Poland', 'Group C', '0 · 0', '23 Nov 2022', '00:00', '', 'FT'),
            ('France vs Australia', 'Group D', '4 · 1', '23 Nov 2022', '03:00', '', 'FT'),
            ('Morocco vs Croatia', 'Group F', '0 · 0', '23 Nov 2022', '18:00', '', 'FT'),
            ('Germany vs Japan', 'Group E', '1 · 2', '23 Nov 2022', '21:00', '', 'FT'),
            ('Spain vs Costa Rica', 'Group E', '7 · 0', '24 Nov 2022', '00:00', '', 'FT'),
            ('Belgium vs Canada', 'Group F', '1 · 0', '24 Nov 2022', '03:00', '', 'FT'),
            ('Switzerland vs Cameroon', 'Group G', '1 · 0', '24 Nov 2022', '18:00', '', 'FT'),
            ('Uruguay vs Korea Republic', 'Group H', '0 · 0', '24 Nov 2022', '21:00', '', 'FT'),
            ('Portugal vs Ghana', 'Group H', '3 · 2', '25 Nov 2022', '00:00', '', 'FT'),
            ('Brazil vs Serbia', 'Group G', '2 · 0', '25 Nov 2022', '03:00', '', 'FT'),
            ('Wales vs Iran', 'Group B', '0 · 2', '25 Nov 2022', '18:00', '', 'FT'),
            ('Qatar vs Senegal', 'Group A', '1 · 3', '25 Nov 2022', '21:00', '', 'FT'),
            ('Netherlands vs Ecuador', 'Group A', '1 · 1', '26 Nov 2022', '00:00', '', 'FT'),
            ('England vs United States', 'Group B', '0 · 0', '26 Nov 2022', '03:00', '', 'FT'),
            ('Tunisia vs Australia', 'Group D', '0 · 1', '26 Nov 2022', '18:00', '', 'FT'),
            ('Poland vs Saudi Arabia', 'Group C', '2 · 0', '26 Nov 2022', '21:00', '', 'FT'),
            ('France vs Denmark', 'Group D', '2 · 1', '27 Nov 2022', '00:00', '', 'FT'),
            ('Argentina vs Mexico', 'Group C', '2 · 0', '27 Nov 2022', '03:00', '', 'FT'),
            ('Japan vs Costa Rica', 'Group E', '0 · 1', '27 Nov 2022', '18:00', '', 'FT'),
            ('Belgium vs Morocco', 'Group F', '0 · 2', '27 Nov 2022', '21:00', '', 'FT'),
            ('Croatia vs Canada', 'Group F', '4 · 1', '28 Nov 2022', '00:00', '', 'FT'),
            ('Spain vs Germany', 'Group E', '1 · 1', '28 Nov 2022', '03:00', '', 'FT'),
            ('Cameroon vs Serbia', 'Group G', '3 · 3', '28 Nov 2022', '18:00', '', 'FT'),
            ('Korea Republic vs Ghana', 'Group H', '2 · 3', '28 Nov 2022', '21:00', '', 'FT'),
            ('Brazil vs Switzerland', 'Group G', '1 · 0', '29 Nov 2022', '00:00', '', 'FT'),
            ('Portugal vs Uruguay', 'Group H', '2 · 0', '29 Nov 2022', '03:00', '', 'FT'),
            ('Netherlands vs Qatar', 'Group A', '2 · 0', '29 Nov 2022', '23:00', '', 'FT'),
            ('Ecuador vs Senegal', 'Group A', '1 · 2', '29 Nov 2022', '23:00', '', 'FT'),
            ('Wales vs England', 'Group B', '0 · 3', '30 Nov 2022', '03:00', '', 'FT'),
            ('Iran vs United States', 'Group B', '0 · 1', '30 Nov 2022', '03:00', '', 'FT'),
            ('Australia vs Denmark', 'Group D', '1 · 0', '30 Nov 2022', '23:00', '', 'FT'),
            ('Tunisia vs France', 'Group D', '1 · 0', '30 Nov 2022', '23:00', '', 'FT'),
            ('Poland vs Argentina', 'Group C', '0 · 2', '1 Dec 2022', '03:00', '', 'FT'),
            ('Saudi Arabia vs Mexico', 'Group C', '1 · 2', '1 Dec 2022', '03:00', '', 'FT'),
            ('Croatia vs Belgium', 'Group F', '0 · 0', '1 Dec 2022', '23:00', '', 'FT'),
            ('Canada vs Morocco', 'Group F', '1 · 2', '1 Dec 2022', '23:00', '', 'FT'),
            ('Japan vs Spain', 'Group E', '2 · 1', '2 Dec 2022', '03:00', '', 'FT'),
            ('Costa Rica vs Germany', 'Group E', '2 · 4', '2 Dec 2022', '03:00', '', 'FT'),
            ('Ghana vs Uruguay', 'Group H', '0 · 2', '2 Dec 2022', '23:00', '', 'FT'),
            ('Korea Republic vs Portugal', 'Group H', '2 · 1', '2 Dec 2022', '23:00', '', 'FT'),
            ('Serbia vs Switzerland', 'Group G', '2 · 3', '3 Dec 2022', '03:00', '', 'FT'),
            ('Cameroon vs Brazil', 'Group G', '1 · 0', '3 Dec 2022', '03:00', '', 'FT'),
            ('Netherlands vs United States', 'Round of 16', '3 · 1', '3 Dec 2022', '23:00', '', 'FT'),
            ('Argentina vs Australia', 'Round of 16', '2 · 1', '4 Dec 2022', '03:00', '', 'FT'),
            ('France vs Poland', 'Round of 16', '3 · 1', '4 Dec 2022', '23:00', '', 'FT'),
            ('England vs Senegal', 'Round of 16', '3 · 0', '5 Dec 2022', '03:00', '', 'FT'),
            ('Japan vs Croatia', 'Round of 16', '1 · 1 (1) · (3)', '5 Dec 2022', '23:00',
             'Croatia wins 3 - 1 on penalties', 'FT'),
            ('Brazil vs Korea Republic', 'Round of 16', '4 · 1', '6 Dec 2022', '03:00', '', 'FT'),
            ('Morocco vs Spain', 'Round of 16', '0 · 0 (3) · (0)', '6 Dec 2022', '23:00',
             'Morocco wins 3 - 0 on penalties', 'FT'),
            ('Portugal vs Switzerland', 'Round of 16', '6 · 1', '7 Dec 2022', '03:00', '', 'FT'),
            ('Croatia vs Brazil', 'Quarter-final', '1 · 1 (4) · (2)', '9 Dec 2022', '23:00',
             'Croatia wins 4 - 2 on penalties', 'FT'),
            ('Netherlands vs Argentina', 'Quarter-final', '2 · 2 (3) · (4)', '10 Dec 2022', '03:00',
             'Argentina wins 4 - 3 on penalties', 'FT'),
            ('Morocco vs Portugal', 'Quarter-final', '1 · 0', '10 Dec 2022', '23:00', '', 'FT'),
            ('England vs France', 'Quarter-final', '1 · 2', '11 Dec 2022', '03:00', '', 'FT'),
            ('Argentina vs Croatia', 'Semi-final', '3 · 0', '14 Dec 2022', '03:00', '', 'FT'),
            ('France vs Morocco', 'Semi-final', '2 · 0', '15 Dec 2022', '03:00', '', 'FT'),
            ('Croatia vs Morocco', 'Play-off for third place', '2 · 1', '17 Dec 2022', '23:00', '', 'FT'),
            ('Argentina vs France', 'Final', '3 · 3 (4) · (2)', '18 Dec 2022', '23:00',
             'Argentina wins 4 - 2 on penalties', 'FT')]
    cursor.executemany(insert_data, data)
    database.commit()


def register_database(connection, database, data_list):
    username = data_list[1]
    password = data_list[2]
    user_type = data_list[3]

    database_message = new_registration(database, username, password, user_type)
    send_message(connection, database_message)


def new_registration(database, username, password, user_type):
    cursor = database.cursor()
    cursor.execute("SELECT username FROM User WHERE username=? AND user_type=?", (username, user_type))

    # Check if the username is registered
    fields = cursor.fetchone()  # It will return a tuple like (password, ) if no data, then return None
    if fields is not None:
        previous_data = fields[0]
        if username == previous_data:
            database_message = 'False Cannot register duplicate username!'
            return database_message

        # If the student is not registered, insert the data into the database
    try:
        cursor.execute("INSERT INTO User (username, password, user_type) VALUES (?, ?, ?)",
                       (username, password, user_type))
        database.commit()
    except Exception as error:
        database_message = f'{False} {error}'
        return database_message
    else:
        database_message = f'{True} {None}'
        return database_message


def query_database(connection, database, data_message, data_list):
    cursor = database.cursor()

    conditions = []
    parameters = []

    for i in range(len(data_message)):
        condition = f"{data_message[i]} LIKE ?"
        parameter = f"%{data_list[i]}%"
        conditions.append(condition)
        parameters.append(parameter)

    query = "SELECT * FROM Tournament WHERE " + " AND ".join(conditions)
    cursor.execute(query, parameters)
    fields = cursor.fetchall()
    reconstitution_data(connection, fields)


def reconstitution_data(connection, data):
    """
    The format of data queried from database is like [(team name, race type, score, data, time, event, status), (...).]
    """
    if len(data) == 0:
        send_message(connection, f'{False}|Cannot query any information to meet the conditions!')
    else:
        elements = ''
        for row in data:
            for column in row:
                elements += column + '_'
            elements = elements.strip('_') + '&'
        else:
            elements = elements.strip('&')
            send_message(connection, f'{True}|{elements}')


def login_database(connection, database, data_list):
    username = data_list[1]
    password = data_list[2]
    user_type = data_list[3]

    database_message = get_registration(database, username, password, user_type)
    send_message(connection, database_message)


def get_registration(database, username, password, user_type):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM User WHERE username=? AND password=? AND user_type=?",
                   (username, password, user_type))

    # Check if the user is registered
    fields = cursor.fetchone()  # It will return a tuple like (password, ) if no data, then return None
    if fields is None:
        database_message = 'False Cannot login unregistered user'
        return database_message
    else:
        database_message = f'{True} {None}'
        return database_message


def insert_database(connection, database, data_list):
    team_name = data_list[1]
    race_type = data_list[2]
    score = data_list[3]
    date = data_list[4]
    race_time = data_list[5]
    event = data_list[6]
    status = data_list[7]

    database_message = insert_race(database, team_name, race_type, score, date, race_time, event, status)
    send_message(connection, database_message)


def insert_race(database, team_name, race_type, score, date, race_time, event, status):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Tournament WHERE team_name=? AND race_type=? AND score=? AND date=? AND time=? "
                   "AND event=? AND status=?", (team_name, race_type, score, date, race_time, event, status))
    # Check if the race is inserted
    fields = cursor.fetchone()  # It will return a tuple like (password, ) if no data, then return None
    if fields is None:
        try:
            cursor.execute("INSERT INTO Tournament VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (team_name, race_type, score, date, race_time, event, status))
            database.commit()
        except Exception as error:
            database_message = f'{False} {error}'
            return database_message
        else:
            database_message = f'{True} {None}'
            return database_message
    else:
        database_message = 'False Cannot add duplicate race!'
        return database_message


def update_database(connection, database, data_list):
    team_name = data_list[1]
    race_type = data_list[2]
    score = data_list[3]
    date = data_list[4]
    race_time = data_list[5]
    event = data_list[6]
    status = data_list[7]

    database_message = update_race(database, team_name, race_type, score, date, race_time, event, status)
    send_message(connection, database_message)


def update_race(database, team_name, race_type, score, date, race_time, event, status):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Tournament WHERE team_name=? AND race_type=? AND score=? AND date=? AND time=? "
                   "AND event=? AND status=?", (team_name, race_type, score, date, race_time, event, status))
    # Check if the race is inserted
    fields = cursor.fetchone()  # It will return a tuple like (password, ) if no data, then return None
    if fields is None:
        try:
            cursor.execute(
                "UPDATE Tournament SET team_name=?, score=?, event=?, status=?WHERE race_type=? AND date=? AND time=?",
                (team_name, score, event, status, race_type, date, race_time))
            database.commit()
        except Exception as error:
            database_message = f'{False} {error}'
            return database_message
        else:
            database_message = f'{True} {None}'
            return database_message
    else:
        database_message = 'False Cannot update duplicate race!'
        return database_message


def get_message(connection, filename):
    database = connect_database(filename)
    while True:
        function_map = receive_response(connection)

        if function_map == '':
            break
        elif function_map[0] == 'r':
            data_list = function_map.split(' ')
            register_database(connection, database, data_list)
        elif function_map[0] == 'q':
            data = function_map.split('|')
            data_message = data[1].split('*')
            data_list = data[2].split('*')
            query_database(connection, database, data_message, data_list)
        elif function_map[0] == 'l':
            data_list = function_map.split(' ')
            login_database(connection, database, data_list)
        elif function_map[0] == 'i':
            data_list = function_map.split('_')
            insert_database(connection, database, data_list)
        elif function_map[0] == 'u':
            data_list = function_map.split('_')
            update_database(connection, database, data_list)


def main():
    filename = os.path.join(os.path.dirname(__file__), "Data.db")
    clients = []
    while True:
        connection, address = connect_client()
        clients.append(connection)
        Thread(target=get_message, args=(connection, filename)).start()


if __name__ == '__main__':
    main()
