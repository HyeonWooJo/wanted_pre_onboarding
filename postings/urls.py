from django.urls import path

from postings.views import PostingView, PostingListView

urlpatterns = [
    path("", PostingView.as_view()),
    path("/<int:posting_id>", PostingView.as_view()),
    path("/list/<int:company_id>", PostingListView.as_view()),
]