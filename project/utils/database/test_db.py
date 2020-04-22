class TestDB:
    _insert = """INSERT INTO test (project_id, name, method_name, status_id, session_id, env) 
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}');"""

    _select_id_by_name = """SELECT id FROM test WHERE name='{}';"""

    def insert(self, project_id, name, method_name, status_id, session_id, env):
        return self._insert.format(project_id, name, method_name, status_id, session_id, env)

    def select_id_by_name(self, name):
        return self._select_id_by_name.format(name)
