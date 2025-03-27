from core.base_test import BaseTest

class TestAuth(BaseTest):

    def test_unauthorized_access_without_token(self):
            response = self.get("contas", headers={})
            self.check_status_code(response, 401)
