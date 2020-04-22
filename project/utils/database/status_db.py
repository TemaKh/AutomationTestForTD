class StatusDB:
    _select_id_by_name = """SELECT id FROM status WHERE name='{}';"""

    _select_id = """SELECT id FROM status"""

    _select_name_by_id = """SELECT name FROM status WHERE id='{}';"""

    def select_id_by_name(self, name):
        return self._select_id_by_name.format(name)

    def select_id(self):
        return self._select_id

    def select_name_by_id(self, status_id):
        return self._select_name_by_id.format(status_id)
