import psycopg2

def initialize_connection():

	# Connection Variables
	DB_NAME="test"
	USER="test"
	PASSWORD="password"
	HOST="127.0.0.1"
	PORT="5432"

	# Create Connection Object
	conn = psycopg2.connect(database=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
	return conn

def destroy_database(table_name):
	# Create Cursor
	conn = initialize_connection()
	curs = conn.cursor()
	
	# Destroy Table
	curs.execute("DROP TABLE " + table_name + ";")
	conn.commit()
	conn.close()
	

def generate_database():
	conn = initialize_connection()
	curs = conn.cursor()
	
	# Generate Users
	with open('users_table.txt', 'r') as file:
		data = file.read().replace('\n', '')
	curs.execute(data)
	conn.commit()
	
	#Generate Messages
		
	conn.close()


def query_username(username, password):
	
	query = "SELECT * FROM users WHERE username='{}' AND password='{}';".format(username, password)
	conn = initialize_connection()
	cur = conn.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	conn.close()

	return rows
