from __init__ import connection, cursor
class Specialty:
    all = []
    def __init__(self, name):
        self.name = name
        self.all.append(self)

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS specialties(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            ); 
        """

        cursor.execute(sql)
        connection.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS Specialties;
        """

        cursor.execute(sql)
        connection.commit()

    def save(self):
        sql = """
            INSERT INTO specialties(name)
            VALUES(?);
        """

        cursor.execute(sql, [self.name])
        connection.commit()

        self.id = cursor.lastrowid


    