from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review),
    path("", views.ReviewView.as_view()),
    # path("thank-you", views.thank_you)
    path("thank-you", views.ThanksView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.ShowReviewView.as_view())
]
