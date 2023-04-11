from db_connection import DBConnection
from neo4j_connection import Neo4jConnection
import json

file = open('credentials.json')
credentials = json.load(file)

db = DBConnection(credentials['mysql'])
neo4j = Neo4jConnection(credentials['neo4j'])

artists = db.get_all('artists')
albums = db.get_all('albums')
songs = db.get_all('songs')
genres = db.get_all('genres')

neo4j.delete_current_graph()
neo4j.get_artists_nodes(artists)
neo4j.get_albums_nodes(albums)
neo4j.get_genres_nodes(genres)
neo4j.get_songs_nodes(songs)



