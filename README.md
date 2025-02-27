Before running `main.py`, create .py file `db_connection.py`
```
import mariadb
import sys

def get_connection():
    try:
        conn = mariadb.connect(
            user="user",
            password="password",
            host="localhost",
            port=3306,
            database="db"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
```
