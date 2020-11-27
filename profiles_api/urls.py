# i created it. this is where the URLs for our API are going to be stored
# first i put smt to urls of profiles_project (include+path)
from django.urls import patch

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]

# first it is going to check the urls from profiles_project.
# the api/ and then the subclasses i 've created here
# the total URL is going to be -> the url address (127.0.0.0.1:8000)/api/hello-view
