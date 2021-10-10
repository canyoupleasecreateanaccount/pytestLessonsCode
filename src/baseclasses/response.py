from src.enums.global_enums import GlobalErrors


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrors.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrors.WRONG_STATUS_CODE.value
        return self
