from django.urls import path
from .views import DetailViewSet, CreateViewSet

urlpatterns = [
    path('<int:pk>/', DetailViewSet.as_view(),),
    path('', CreateViewSet.as_view(), )

]