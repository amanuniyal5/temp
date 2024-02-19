from flask import Flask, request, jsonify
import mysql.connector
import hashlib

app = Flask(__name__)

from prettytable import PrettyTable

hostname = "sql6.freemysqlhosting.net"
username = "sql6685246"
password = "yMnAwzlc3e"
database = "sql6685246"

def create_tables():
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor=connection.cursor()
            query="""CREATE TABLE  IF NOT EXISTS user_details(
                name varchar(1000),
                user_name varchar(1000) ,
                email varchar(1000) ,
                password varchar(1000) ,
                user_id INT AUTO_INCREMENT PRIMARY KEY);"""
            cursor.execute(query)
            connection.commit()
            query="""CREATE TABLE  IF NOT EXISTS  images(
            image_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT  ,
            image LONGBLOB,
            metadata varchar(1000)
            );"""
            cursor.execute(query)
            connection.commit()
            query="""CREATE TABLE  IF NOT EXISTS audio(
                audio_id INT AUTO_INCREMENT PRIMARY KEY,
                audio_data LONGBLOB,
                audio_metadata varchar(1000)
            );"""
            cursor.execute(query)
            connection.commit()
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

def insert_data(name1,username1, email1, password1):
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()
            query = "INSERT INTO user_details (name,user_name, email, password) VALUES (%s,%s, %s, %s)"
            data = (name1,username1, email1, password1)
            cursor.execute(query, data)
            connection.commit()

            print("Data inserted successfully!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")




def print_table_from_mysql():
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )


        if connection.is_connected():
            print("Connected to MySQL database")

           
            cursor = connection.cursor()

            
            query = "SELECT * FROM user_details"
            cursor.execute(query)

            
            rows = cursor.fetchall()

           
            if rows:
                columns = [column[0] for column in cursor.description]
                table = PrettyTable(columns)
                table.align = 'l' 

                for row in rows:
                    table.add_row(row)

                print(table)
            else:
                print("No data found in the table.")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")



@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Encrypt password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert user data into the database
    insert_data(username, name, email, hashed_password)

    return jsonify({'message': 'Signup successful'})

 
if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
