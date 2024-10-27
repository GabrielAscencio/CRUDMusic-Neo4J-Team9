from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
#import drivers

#URI = borrado, disponible desde os.getenv("DB_URI")
#AUTH = borrado, disponible desde (os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))

#Variables de entorno
load_dotenv()
envedURI = os.getenv("DB_URI")
envedAUTH = (os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))

with GraphDatabase.driver(envedURI, auth=envedAUTH) as driver:
    driver.verify_connectivity()

# Conectar a la base de datos Neo4j
class Neo4jCRUD:
    def __init__(self, uri, user, password):
        # Inicializamos el driver para conectarnos a Neo4j
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Cerramos la conexión a la base de datos
        self.driver.close()

    # Crear un nodo persona
    def crear_persona(self, nombre, edad):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._crear_nodo_persona, nombre, edad)

    @staticmethod
    def _crear_nodo_persona(tx, nombre, edad):
        # Cypher es el lenguaje de consultas de Neo4j
        query = "CREATE (p:Persona {nombre: $nombre, edad: $edad})"
        tx.run(query, nombre=nombre, edad=edad)
        print(f"Persona '{nombre}' creada correctamente.")

    # Leer todos los nodos de tipo Persona
    def leer_personas(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._leer_nodos_persona)
            for record in result:
                print(f"Nombre: {record['nombre']}, Edad: {record['edad']}")

    @staticmethod
    def _leer_nodos_persona(tx):
        # Consulta Cypher para leer todas las personas
        query = "MATCH (p:Persona) RETURN p.nombre AS nombre, p.edad AS edad"
        result = tx.run(query)
        return [record for record in result]

    # Actualizar la edad de una persona según su nombre
    def actualizar_persona(self, nombre, nueva_edad):
        with self.driver.session() as session:
            session.write_transaction(self._actualizar_nodo_persona, nombre, nueva_edad)

    @staticmethod
    def _actualizar_nodo_persona(tx, nombre, nueva_edad):
        query = "MATCH (p:Persona {nombre: $nombre}) SET p.edad = $nueva_edad"
        tx.run(query, nombre=nombre, nueva_edad=nueva_edad)
        print(f"Persona '{nombre}' actualizada a {nueva_edad} años.")

    # Eliminar un nodo Persona según su nombre
    def eliminar_persona(self, nombre):
        with self.driver.session() as session:
            session.write_transaction(self._eliminar_nodo_persona, nombre)

    @staticmethod
    def _eliminar_nodo_persona(tx, nombre):
        query = "MATCH (p:Persona {nombre: $nombre}) DELETE p"
        tx.run(query, nombre=nombre)
        print(f"Persona '{nombre}' eliminada correctamente.")

# Uso del CRUD con Neo4j
if __name__ == "__main__":
    # Cambia estos valores según tu configuración de Neo4j
    uri = envedURI  # La URI del servidor Neo4j
    user = os.getenv("DB_USER")  # Usuario de Neo4j
    password = os.getenv("DB_PASSWORD")  # Contraseña del usuario

    # Crear una instancia de la clase Neo4jCRUD
    neo4j_crud = Neo4jCRUD(uri, user, password)

    # Crear personas
    neo4j_crud.crear_persona("Carlos", 28)
    neo4j_crud.crear_persona("María", 34)

    # Leer todas las personas
    print("Lista de personas en la base de datos:")
    neo4j_crud.leer_personas()

    # Actualizar la edad de una persona
    neo4j_crud.actualizar_persona("Carlos", 29)

    # Eliminar una persona
    neo4j_crud.eliminar_persona("María")

    # Leer personas nuevamente para verificar cambios
    print("Lista de personas después de los cambios:")
    neo4j_crud.leer_personas()

    # Cerrar la conexión a la base de datos
    neo4j_crud.close()
