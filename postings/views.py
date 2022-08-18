import json

from django.http  import JsonResponse
from django.views import View

from postings.models  import Posting
from companies.models import Company

class PostingView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            company = Company.objects.get(name=data['name'])

            posting, is_created = Posting.objects.update_or_create(
                position = data['position'],
                reward   = data['reward'],
                content  = data['content'],
                stack    = data['stack'],
                defaults = {
                    'company'  : company
                }
            )

            status_code = 201 if is_created else 200

            return JsonResponse({'message' : 'SUCCESS'}, status = status_code)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    def delete(self, request):
        try:
            data    = json.loads(request.body)
            posting = Posting.objects.get(id=data['id'])
            posting.delete()

            return JsonResponse({'message' : 'DATA_DELETED'}, status = 204)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except Posting.DoesNotExist:
            return JsonResponse({'message' : 'DATA_DOES_NOT_EXIST'}, status = 400)

    def get(self, request, posting_id):
        posting  = Posting.objects.get(id=posting_id)
        postings = Posting.objects.filter(company=posting.company)

        posting = {
            "posting_id"        : posting.id,
            "name"              : posting.company.name,
            "country"           : posting.company.country,
            "location"          : posting.company.location,
            "position"          : posting.position,
            "reward"            : posting.reward,
            "stack"             : posting.stack,
            "other_postings_id" : [postingg.id for postingg in postings if postingg.id != posting.id ]
        }

        return JsonResponse({'result' : posting}, status = 200)

class PostingSearchView(View):
    def get(self, request):
        company_name = request.GET.get('company_name', None)
        company      = Company.objects.get(name=company_name)
        postings     = Posting.objects.filter(company=company)

        posting_list = [{   
            "posting_id" : posting.id,
            "name"       : company.name,
            "country"    : company.country,
            "location"   : company.location,
            "position"   : posting.position,
            "reward"     : posting.reward,
            "stack"      : posting.stack
        } for posting in postings]

        return JsonResponse({'results' : posting_list}, status = 200)


class PostingListView(View):
    def get(self, request, company_id):
        company  = Company.objects.get(id=company_id)
        postings = Posting.objects.filter(company=company)

        posting_list = [{   
            "posting_id" : posting.id,
            "name"       : company.name,
            "country"    : company.country,
            "location"   : company.location,
            "position"   : posting.position,
            "reward"     : posting.reward,
            "stack"      : posting.stack
        } for posting in postings]

        return JsonResponse({'results' : posting_list}, status = 200)