#Hola mundo de ejemplo para ejecuciones de conexión
#El primer hola es una prueba de salida
#El Segundo es una prueba de conexión a la GraphDB

print("PY OUTPUT: "+"Hola Mundos")

from neo4j import GraphDatabase

uri = "neo4j+ssc://c8ef140e.databases.neo4j.io"   #Aura URI
#uri = "bolt://localhost:7687"                       #Bolt URI
password = "3zgQO7OqqktPEGgDAW7gF_8C0C-50iE_CDCmSG8SZqk"
user = "neo4j"

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample(uri, user, password)
    greeter.print_greeting("hello, world")
    greeter.close()