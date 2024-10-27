from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError

load_dotenv()
envedURI = os.getenv("DB_URI")
envedAUTH = (os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))

#DFuncion para probar la conexion y ya
def test_connection_env():
    try:
        print("--Iniciando prueba con variables de entorno--")
        # Intentar la conexión
        with GraphDatabase.driver(envedURI, auth=envedAUTH) as driver:
            print("Enved> Intentando conectar a la instancia " +
            os.getenv("AURA_INSTANCEID") + " de " + 
            os.getenv("AURA_INSTANCEOWNERALIAS") + ".")
            driver.verify_connectivity()
            print("Enved> Conexión exitosa a la base de datos " +
                 os.getenv("AURA_INSTANCENAME") + ".")
    except ServiceUnavailable:
        print("Enved> No se pudo conectar al servicio de la instancia " +
             os.getenv("AURA_INSTANCEID") + " de " + 
             os.getenv("AURA_INSTANCEOWNERALIAS") + " " +
             "Verifique la URI o el estado del servidor.")
    except AuthError:
        print("Enved> Error de autenticación. Verifique el nombre de usuario y contraseña.")
    except Exception as e:
        print(f"Enved> Ocurrió un error inesperado: {e}")

# Ejecutar prueba de conexión sin env
test_connection_env()
