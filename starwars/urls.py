from starwars.views import StarItemView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('star/', StarItemView.as_view()),

]

urlpatterns += router.urls
