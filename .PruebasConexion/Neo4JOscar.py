#LEER: Este es un test para conexión directa a la intancia Aura de Oscar
from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError


# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+ssc://c8ef140e.databases.neo4j.io"
AUTH = ("neo4j", "3zgQO7OqqktPEGgDAW7gF_8C0C-50iE_CDCmSG8SZqk")

load_dotenv()
envedURI = os.getenv("DB_URI")
envedAUTH = (os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))
envedowner = (os.getenv("AURA_INSTANCEALIAS"))


#####Prueba extendida con excepciones
#Solo debe decir conexion exitosa o que falló en caso de.
def test_connection():
    try:
        # Intentar la conexión
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            driver.verify_connectivity()
            print("Conexión exitosa a la base de datos.")
    except ServiceUnavailable:
        print("No se pudo conectar al servicio. Verifique la URI o el estado del servidor.")
    except AuthError:
        print("Error de autenticación. Verifique el nombre de usuario y contraseña.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def test_connection_env():
    try:
        print("Iniciando prueba con variables de entorno")
        # Intentar la conexión
        with GraphDatabase.driver(envedURI, auth=envedAUTH) as driver:
            driver.verify_connectivity()
            print("Enved> Si ves esto se realiz+o exitosamente la conexión a la base de datos de OZKAR.")
            print("Enved> de" + envedowner)
    except ServiceUnavailable:
        print("Enved> No se pudo conectar al servicio. Verifique la URI o el estado del servidor.")
    except AuthError:
        print("Enved> Error de autenticación. Verifique el nombre de usuario y contraseña.")
    except Exception as e:
        print(f"Enved> Ocurrió un error inesperado: {e}")

# Ejecutar prueba de conexión sin env
test_connection()

# Ahora con env
test_connection_env()