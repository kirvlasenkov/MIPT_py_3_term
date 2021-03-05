import sqlite3
import os
from dotenv import load_dotenv

# Downloading of environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DATABASE = os.getenv("DATABASE")


class CursorError(Exception):
    pass


class ConnectionError(Exception):
    pass


class SqlDataBase:

    def __init__(self, database):
        self.__connection = sqlite3.connect(database)
        self.__cursor = self.__connection.cursor()

    def create_table(self, force=False) -> None:
        if force:
            self.__cursor.execute("DROP TABLE IF EXISTS favourite_phrases")

        self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS favourite_phrases (
                ID           INTEGER  PRIMARY KEY,
                USER_ID      INTEGER  NOT NULL,
                USER_NAME    TEXT     NOT NULL,
                ADDED_PHRASE TEXT     NOT NULL,
                CONSTRAINT 'fk users' FOREIGN KEY (USER_ID) REFERENCES users (USER_ID)
                );
            """)
        self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                USER_ID INTEGER PRIMARY KEY,
                USER_NAME TEXT NOT NULL
                ); """)
        self.__connection.commit()

    def add_favourite_phrase(self, id: int, user_name: str, phrase: str):
        self.__cursor.execute('INSERT INTO favourite_phrases (USER_ID, ADDED_PHRASE, USER_NAME)'
                              ' VALUES (?, ?, ?)', (id, phrase, user_name))
        self.__connection.commit()

    def get_favourite_phrases(self, id: int):
        pass

    def delete_favourite_phrase(self, id: int):
        self.__cursor.execute("DELETE FROM favourite_phrases WHERE USER_ID = {}".format(id))
        self.__connection.commit()

    def close(self):
        self.__connection.close()


if __name__ == "__main__":
    database = SqlDataBase("data.db")
    database.create_table(force=True)