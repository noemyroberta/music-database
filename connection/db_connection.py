import mysql.connector


class DBConnection:

    def __init__(self, credential: dict):
        print("Creating connection...")
        self.db = mysql.connector.connect(
            host=credential['host'],
            user=credential['user'],
            password=credential['password'],
            database=credential['database']
        )
        self.manager = self.db.cursor()

    def get_all(self, tb_name):
        print("Getting all %s" % tb_name)
        self.manager.execute("SELECT * FROM tb_%s" % tb_name)
        result = self.manager.fetchall()
        return result

    def close(self):
        self.manager.close()
        self.db.close()
