from google.cloud.sql.connector import Connector
import sqlalchemy
from dotenv import load_dotenv, find_dotenv
import numpy as np
from typing import List, Optional
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel
import os

_ = load_dotenv(find_dotenv())

project_id = os.environ["PROJECT_ID"]
region = os.environ["REGION"]
instance_name = os.environ["INSTANCE_NAME"]

# initialize parameters
INSTANCE_CONNECTION_NAME = f"{project_id}:{region}:{instance_name}" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]

def embed_text(
    texts: List[str] = ["banana muffins? ", "banana bread? banana muffins?"],
    task: str = "RETRIEVAL_DOCUMENT",
    model_name: str = "text-embedding-004",
    dimensionality: Optional[int] = 256,
) -> List[List[float]]:
    """Embeds texts with a pre-trained, foundational model."""
    model = TextEmbeddingModel.from_pretrained(model_name)
    inputs = [TextEmbeddingInput(text, task) for text in texts]
    kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
    embeddings = model.get_embeddings(inputs, **kwargs)
    return [embedding.values for embedding in embeddings]

embedding = np.array(embed_text(["text encoded"])[0])

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

  # query and fetch ratings table
#   results = db_conn.execute(sqlalchemy.text("SELECT * FROM ratings")).fetchall()
    results = db_conn.execute(sqlalchemy.text("SELECT * FROM items ORDER BY embedding <-> %s LIMIT 10", (embedding,))).fetchall()

  # show results
    for row in results:
        print(row)

connector.close()