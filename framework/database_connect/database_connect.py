import pymysql


class DatabaseConnect:

    def __init__(self, host, port, login, password, db):
        self._connect = pymysql.connect(host=host,
                                        port=port,
                                        user=login,
                                        password=password,
                                        db=db,
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor,
                                        autocommit=True)

    def get_connect(self):
        return self._connect

    def close_connect(self):
        self._connect.close()
