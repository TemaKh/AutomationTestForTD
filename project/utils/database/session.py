class Session:
    _select_id = """SELECT id FROM `session`;"""

    def select_id(self):
        return self._select_id
