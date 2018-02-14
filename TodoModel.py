import psycopg2
import psycopg2.extras


class Todo:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="todo",
                user="postgres",
                host='127.0.0.1',
                password='123456'
            )
            print("Connected")
        except psycopg2.Error as e:
            print("I am unable to connect to the database", e)

    def get_todos(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * from todos")
        todos = cursor.fetchall()
        self.conn.close()
        return todos

    def save_todo(self, todo_name):
        print("todo_name: {}".format(todo_name))
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("""
            INSERT INTO todos (todo_name)
            VALUES (%(todo_name)s)
        """, dict(
            todo_name=todo_name,
        ))
        self.conn.commit()
        self.conn.close()

    def delete_todo(self, todo_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("""
            DELETE from todos where id=%(todo_id)s
        """, dict(
            todo_id=todo_id,
        ))
        self.conn.commit()
        self.conn.close()
