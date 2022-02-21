"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8. **Achtung**: der OAuth header muss 'OAuthAccessToken' heißen.<br><br> Die API verfügt außerdem nicht über ein gültiges TLS Zertifikat. Deswegen sollte die TLS-Validierung deaktiviert werden.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.jobsuche.api.default_api import DefaultApi  # noqa: E501

from deutschland import jobsuche


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ed_v1_arbeitgeberlogo_hash_id_get(self):
        """Test case for ed_v1_arbeitgeberlogo_hash_id_get

        Unternehmen Logo  # noqa: E501
        """
        pass

    def test_pc_v2_app_jobs_hash_id_bewerbung_get(self):
        """Test case for pc_v2_app_jobs_hash_id_bewerbung_get

        Bewerbung Kontaktdaten  # noqa: E501
        """
        pass

    def test_pc_v2_jobdetails_hash_id_get(self):
        """Test case for pc_v2_jobdetails_hash_id_get

        Jobdetail  # noqa: E501
        """
        pass

    def test_pc_v4_app_jobs_get(self):
        """Test case for pc_v4_app_jobs_get

        Jobsuche  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
