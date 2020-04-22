class Log:
    _insert = """INSERT INTO log (content, is_exception, test_id) VALUES ('{}', '{}', '{}');"""

    _select_content = """SELECT content FROM log WHERE test_id = '{}';"""

    def insert(self, content, is_exception, test_id):
        return self._insert.format(content, is_exception, test_id)

    def select_content(self, test_id):
        return self._select_content.format(test_id)
