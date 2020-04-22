class Attachment:
    _insert = """INSERT INTO attachment (content, content_type, test_id) VALUES (%s, '{}', '{}');"""

    _select_content = """SELECT content FROM attachment WHERE test_id = '{}';"""

    def insert(self, content_type, test_id):
        return self._insert.format(content_type, test_id)

    def select_content(self, test_id):
        return self._select_content.format(test_id)
