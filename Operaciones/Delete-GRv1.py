# Métodos para eliminar nodos
def eliminar_artista(self, id):
    with self.driver.session(database="neo4j") as session:
        artista = session.read_transaction(self._obtener_artista, id)
        if artista:
            print(f"Se va a eliminar el artista: {artista}")
            if self._confirmar_borrado():
                session.write_transaction(self._eliminar_nodo_artista, id)
                print(f"Artista con ID {id} eliminado.")
            else:
                print("Eliminación cancelada.")
        else:
            print(f"No se encontró un artista con ID {id}.")

@staticmethod
def _obtener_artista(tx, id):
    query = "MATCH (artist:Artist {id: $id}) RETURN artist"
    result = tx.run(query, id=id)
    return result.single()

@staticmethod
def _eliminar_nodo_artista(tx, id):
    query = "MATCH (artist:Artist {id: $id}) DELETE artist"
    tx.run(query, id=id)

def eliminar_album(self, id):
    with self.driver.session(database="neo4j") as session:
        album = session.read_transaction(self._obtener_album, id)
        if album:
            print(f"Se va a eliminar el álbum: {album}")
            if self._confirmar_borrado():
                session.write_transaction(self._eliminar_nodo_album, id)
                print(f"Álbum con ID {id} eliminado.")
            else:
                print("Eliminación cancelada.")
        else:
            print(f"No se encontró un álbum con ID {id}.")

@staticmethod
def _obtener_album(tx, id):
    query = "MATCH (album:Album {id: $id}) RETURN album"
    result = tx.run(query, id=id)
    return result.single()

@staticmethod
def _eliminar_nodo_album(tx, id):
    query = "MATCH (album:Album {id: $id}) DELETE album"
    tx.run(query, id=id)

def eliminar_cancion(self, id):
    with self.driver.session(database="neo4j") as session:
        cancion = session.read_transaction(self._obtener_cancion, id)
        if cancion:
            print(f"Se va a eliminar la canción: {cancion}")
            if self._confirmar_borrado():
                session.write_transaction(self._eliminar_nodo_cancion, id)
                print(f"Canción con ID {id} eliminada.")
            else:
                print("Eliminación cancelada.")
        else:
            print(f"No se encontró una canción con ID {id}.")

@staticmethod
def _obtener_cancion(tx, id):
    query = "MATCH (song:Song {id: $id}) RETURN song"
    result = tx.run(query, id=id)
    return result.single()

@staticmethod
def _eliminar_nodo_cancion(tx, id):
    query = "MATCH (song:Song {id: $id}) DELETE song"
    tx.run(query, id=id)

# Métodos para eliminar relaciones
def eliminar_relacion_artista_album(self, artist_name, album_name):
    with self.driver.session(database="neo4j") as session:
        print(f"Se va a eliminar la relación entre el artista '{artist_name}' y el álbum '{album_name}'.")
        if self._confirmar_borrado():
            session.write_transaction(self._eliminar_relacion_artista_album, artist_name, album_name)
            print(f"Relación entre '{artist_name}' y '{album_name}' eliminada.")
        else:
            print("Eliminación cancelada.")

@staticmethod
def _eliminar_relacion_artista_album(tx, artist_name, album_name):
    query = """
    MATCH (artist:Artist {Name: $artist_name})-[r:ARTIST_OF]->(album:Album {Name: $album_name})
    DELETE r
    """
    tx.run(query, artist_name=artist_name, album_name=album_name)

# Método de confirmación
def _confirmar_borrado(self):
    confirmacion = input("¿Está seguro de que desea continuar con la eliminación? (sí/no): ")
    return confirmacion.lower() == "sí"
