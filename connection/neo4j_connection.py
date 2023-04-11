from neo4j import GraphDatabase


class Neo4jConnection:

    def __init__(self, credential: dict):
        print("Creating new session for Neo4j...")
        self.driver = GraphDatabase.driver(credential['url'], auth=(credential['user'], credential['password']))
        self.session = self.driver.session()

    def delete_graph_constraints(self):
        constraints = self.session.run('CALL db.constraints')
        for constraint in constraints:
            self.session.run("DROP " + constraint['description'])

    def delete_current_graph(self):
        self.session.run("MATCH (n) DETACH DELETE n;")
        self.delete_graph_constraints()

    def show_graph(self):
        self.session.run("MATCH (n) RETURN n;")

    def set_graph_constraints(self):
        self.session.run("CREATE CONSTRAINT ON (g:Genre) ASSERT g.name IS UNIQUE")
        self.session.run("CREATE CONSTRAINT ON (a:Album) ASSERT a.id IS UNIQUE")
        self.session.run("CREATE CONSTRAINT ON (a:Artist) ASSERT a.id IS UNIQUE")
        self.session.run("CREATE CONSTRAINT ON (s:Song) ASSERT s.id IS UNIQUE")

    def get_artists_nodes(self, artists):
        print("Creating nodes for artists...")
        for artist in artists:
            query = "CREATE (:Artist {id: '%s', name: '%s', bio: '%s', country: '%s'})" % (
                artist[0], artist[1], artist[2], artist[3])
            self.session.run(query)

    def get_genres_nodes(self, genres):
        print("Creating nodes for genres...")
        for genre in genres:
            query = "CREATE (:Genre {id: '%s', name: '%s'})" % (genre[0], genre[1])
            self.session.run(query)

    def get_albums_nodes(self, albums):
        print("Creating nodes for albums...")
        for album in albums:
            query = "CREATE (:Album {id: '%s', name: '%s', release_year: '%s', artist: '%s', genre: '%s'})" % (
                album[0], album[1], album[2], album[3], album[4])
            self.session.run(query)

    def get_songs_nodes(self, songs):
        print("Creating nodes for songs...")
        for song in songs:
            query = "CREATE (:Song {id: '%s', name: '%s', album: '%s', duration: '%s', lyrics: '%s'})" % (
                song[0], song[1], song[2], song[3], song[4])
            self.session.run(query)

    def get_graph_relationships(self, album_artists):
        self.session.run("MATCH (s:Song), (a:Album{id: s.album}) CREATE (s)-[:IN_ALBUM]->(a);")
        self.session.run("MATCH (a:Album), (ar:Artist{id: a.artist}) CREATE (a)-[:IS_FROM]->(ar);")
        self.session.run("MATCH (ar:Artist), (a:Album{artist: ar.id}) CREATE (ar)-[:IS_SINGER]->(a);")
        self.session.run("MATCH (a:Album), (g:Genre{id: a.genre}) CREATE (a)-[:HAS_GENRE]->(g);")

        if album_artists:
            for alb in album_artists:
                self.session.run(
                    "MATCH (ar:Artist), (a:Album) "
                    "WHERE a.id = '%s' AND ar.id = '%s' " % (alb[0], alb[1]) +
                    "CREATE (ar)-[:IS_SINGER]->(a)"
                )
