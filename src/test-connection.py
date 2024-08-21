from google.cloud.sql.connector import Connector
import sqlalchemy

project_id = "posgresql-433015 "
region = "us-central1"
instance_name = "pgvec"

# initialize parameters
INSTANCE_CONNECTION_NAME = f"{project_id}:{region}:{instance_name}" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "an"
DB_PASS = "qr4nIeL  "
DB_NAME = "pgvec-db"


embedding = #vector

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

# connect to connection pool
with pool.connect() as db_conn:
  # create ratings table in our sandwiches database
#   db_conn.execute(
#     sqlalchemy.text(
#       "CREATE TABLE IF NOT EXISTS ratings "
#       "( id SERIAL NOT NULL, name VARCHAR(255) NOT NULL, "
#       "origin VARCHAR(255) NOT NULL, rating FLOAT NOT NULL, "
#       "PRIMARY KEY (id));"
#     )
#   )

#   # commit transaction (SQLAlchemy v2.X.X is commit as you go)
#   db_conn.commit()

#   # insert data into our ratings table
#   insert_stmt = sqlalchemy.text(
#       "INSERT INTO ratings (name, origin, rating) VALUES (:name, :origin, :rating)",
#   )

#   # insert entries into table
#   db_conn.execute(insert_stmt, parameters={"name": "HOTDOG", "origin": "Germany", "rating": 7.5})
#   db_conn.execute(insert_stmt, parameters={"name": "BÀNH MÌ", "origin": "Vietnam", "rating": 9.1})
#   db_conn.execute(insert_stmt, parameters={"name": "CROQUE MADAME", "origin": "France", "rating": 8.3})

#   # commit transactions
#   db_conn.commit()

  # query and fetch ratings table
#   results = db_conn.execute(sqlalchemy.text("SELECT * FROM ratings")).fetchall()
    results = db_conn.execute(sqlalchemy.text("SELECT * FROM items ORDER BY embedding <-> %s LIMIT 10", (embedding,))).fetchall()

  # show results
    for row in results:
        print(row)

connector.close()