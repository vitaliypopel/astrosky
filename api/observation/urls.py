from django.urls import path

from .views import ObserveAPIView, ObserveManyAPIView

app_name = 'observation'
urlpatterns = [
    path('observe/', ObserveAPIView.as_view(), name='observe'),
    path('observe/many/', ObserveManyAPIView.as_view(), name='observe-many'),
]
