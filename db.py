import psycopg2

# Helper functions to access the database

# Function given postgres server details will return a connection
def initialize_connection():

	# Connection Variables
	DB_NAME= "XXXXX"
	USER="XXXXX"
	PASSWORD="XXXXX"
	HOST="127.0.0.1"
	PORT="5432"

	# Create Connection Object
	conn = psycopg2.connect(database=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
	return conn

# Helper function to destroy a table
def destroy_database(table_name):
	# Create Cursor
	conn = initialize_connection()
	curs = conn.cursor()
	
	# Destroy Table
	curs.execute("DROP TABLE " + table_name + ";")
	conn.commit()
	conn.close()
	
# Helper function to generate a table with dummy data (must have text file with a query)
def generate_database(table_name):
	conn = initialize_connection()
	curs = conn.cursor()
	
	# Generate Users
	data_file = table_name + "_table.txt"
	with open(data_file, 'r') as file:
		data = file.read().replace('\n', '')
	curs.execute(data)
	conn.commit()
	conn.close()

# Function that will create a query to check the database for login credentials
def query_username(username, password):
	
	query = "SELECT * FROM users WHERE username='{}' AND password='{}';".format(username, password)
	conn = initialize_connection()
	cur = conn.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	conn.close()

	return rows

# Function that will INSERT INTO the "posts" table and return the output
def query_posts(message):
	
	query = "INSERT INTO posts (message_id, time_posted, author, post) values (101, '01/14/2020', 'crounds3', '{}') RETURNING post;".format(message)
	conn = initialize_connection()
	cur = conn.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	conn.close()

	return rows
