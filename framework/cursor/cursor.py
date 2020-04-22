class Cursor:

    def __init__(self, connect):
        self._connect = connect

    def execute_query_insert(self, query):
        with self._connect.cursor() as cursor:
            cursor.execute(query)
            self._connect.commit()
            return cursor

    def execute_query_select(self, query):
        with self._connect.cursor() as cursor:
            cursor.execute(query)
            return cursor

    def execute_query_insert_image(self, query, image):
        with self._connect.cursor() as cursor:
            cursor.execute(query, image)
            self._connect.commit()
            return cursor
