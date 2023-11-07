import sqlite3
import configuration

class Database:

    def createDatabase(self, db_name = "./../data/{}".format(configuration.DATABASE_NAME) ) -> None:    
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS paper (
                url TEXT PRIMARY KEY,
                theme TEXT,
                timestamp TEXT,
                content TEXT
            )
        ''')
        self.conn.commit()
        self.conn.close()

    

#if __name__ == '__main__':
#    DB = Database().createDatabase("./../data/cs.db")
    