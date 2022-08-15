import json

from django.test import TestCase, Client

from postings.models  import Posting
from companies.models import Company

class PostingView(TestCase):
    def setUp(self):
        Posting.objects.create(
            id       = 1,
            position = 'Back-end',
            reward   = 400000,
            content  = 'company1에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..',
            stack    = 'Django'
        )

        Posting.objects.create(
            id       = 2,
            position = 'Back-end',
            reward   = 400000,
            content  = 'company1에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..',
            stack    = 'Django'
        )

        Posting.objects.create(
            id       = 3,
            position = 'Back-end',
            reward   = 400000,
            content  = 'company1에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..',
            stack    = 'Django'
        )

        Company.objects.create(
            id       = 1,
            name     = 'company1',
            country  = 'Korea',
            location = 'Seoul',
            posting  = Posting.objects.get(id=1)
        )

    def tearDown(self):
        Posting.objects.all().delete()
        Company.objects.all().delete()

    def test_success_posting_view_post(self):
        client   = Client()
        body     = {
                    'position' : 'Back-end',
                    'reward'   : 200000,
                    'content'  : '백엔드 채용합니다.',
                    'stack'    : 'Node.js'
                }
        response = client.post("/postings", content_type='application/json', data=json.dumps(body))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'SUCCESS'})

    def test_key_error_posting_view_post(self):
        client   = Client()
        body     = {
                    'position1' : 'Back-end',
                    'reward'   : 200000,
                    'content'  : '백엔드 채용합니다.',
                    'stack'    : 'Node.js'
                }
        response = client.post("/postings", content_type='application/json', data=json.dumps(body))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})

    def test_success_posting_view_delete(self):
        client   = Client()
        body     = {
                    'id' : 1
                }
        response = client.delete("/postings", content_type='application/json', data=json.dumps(body))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json(), {'message' : 'DATA_DELETED'})

    def test_key_error_posting_view_delete(self):
        client   = Client()
        body     = {
                    'id1' : 1
                }
        response = client.delete("/postings", content_type='application/json', data=json.dumps(body))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})

    def test_key_error_posting_view_delete(self):
        client   = Client()
        body     = {
                    'id' : 15
                }
        response = client.delete("/postings", content_type='application/json', data=json.dumps(body))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'DATA_DOES_NOT_EXIST'})

    def test_success_posting_view_get(self):
        client   = Client()
        response = client.get("/postings/1", content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"RESULT" : {
            "posting_id"     : 1,
            "name"           : 'company1',
            "country"        : 'Korea',
            "location"       : 'Seoul',
            "position"       : 'Back-end',
            "reward"         : 400000,
            "stack"          : 'Django',
            "other_postings" : [postingg.id for postingg in postings if postingg.id != posting.id ]
        }}
)