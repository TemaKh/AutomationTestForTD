class ResponseApi:

    def __init__(self, status_code, response):
        self._status_code = status_code
        self._response = response

    def get_status_code(self):
        return self._status_code

    def get_response(self):
        return self._response
