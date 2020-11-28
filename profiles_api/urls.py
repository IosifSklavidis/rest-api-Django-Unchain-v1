# i created it. this is where the URLs for our API are going to be stored
# first i put smt to urls of profiles_project (include+path)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


# for viewsets i need routers!! + to vazw kai sto urlpatterns
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
# in the 2 router i dont provide a base_name due to the queryset in my views.
router.register('feed',views.UserProfileViewset)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]

# first it is going to check the urls from profiles_project.
# the api/ and then the subclasses i 've created here
# the total URL is going to be -> the url address (127.0.0.0.1:8000)/api/hello-view
