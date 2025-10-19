from django.urls import path
from .views import SVMClassifierView

urlpatterns = [
    path("svm/", SVMClassifierView.as_view(), name="svm_api"),
]
