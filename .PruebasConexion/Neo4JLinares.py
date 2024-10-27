from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError

load_dotenv()

URI = os.getenv("DB_URI")
AUTH = (os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))

def test_connection(uri, auth):
    """
    Attempts to connect to the Neo4j database using the provided URI and auth tuple.
    """
    try:
        with GraphDatabase.driver(uri, auth=auth) as driver:
            driver.verify_connectivity()
            print("Conexión exitosa a la base de datos.")
    except ServiceUnavailable:
        print("No se pudo conectar al servicio. Verifique la URI o el estado del servidor.")
    except AuthError:
        print("Error de autenticación. Verifique el nombre de usuario y contraseña.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if URI and all(AUTH):
    print("Iniciando prueba de conexión con variables de entorno")
    test_connection(URI, AUTH)
else:
    print("Error: Uno o más variables de entorno no están configuradas correctamente.")
