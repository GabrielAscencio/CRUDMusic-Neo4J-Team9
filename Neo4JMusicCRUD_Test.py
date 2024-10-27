from dotenv import load_dotenv
import os
from Neo4JMusicCRUD import MusicDatabaseCRUD

# Cargar el archivo
load_dotenv()
uri = os.getenv("DB_URI")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Conectar a la BD
db = MusicDatabaseCRUD(uri, user, password)
session = db.driver.session(database="neo4j")

# Replace
session.run("""
MATCH (a:Artist {id: 1})
SET a = {id: 1, Name: 'Juan', Lastname: 'López', Nationality: 'Colombiano'}
""")
session.run("""
MATCH (a:Artist {id: 2})
SET a = {id: 2, Name: 'María', Lastname: 'Martínez', Nationality: 'Argentina'}
""")

#Update
session.run("""
MATCH (a:Artist {id: 1})
SET a.Name = 'Juan Carlos'
""")
session.run("""
MATCH (a:Artist {id: 2})
SET a.Name = 'Maria Fernanda'
""")

# Delete
session.run("""
MATCH (a:Artist {id: 1})
DELETE a
""")

# Cerrar la sesión y BD
session.close()
db.close()
