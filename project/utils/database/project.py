class Project:
    _select_id_by_name = """SELECT id FROM project WHERE name='{}';"""

    def select_id_by_name(self, name):
        return self._select_id_by_name.format(name)
