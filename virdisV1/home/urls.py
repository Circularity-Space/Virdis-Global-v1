from django.conf.urls import url
from . import views

app_name = "home"

urlpatterns = [
    url("^$",views.homeView,name = "home"),
    url("^android-app/$",views.download_file,name="download-app"),
    url("^team/$",views.teamView, name = "team"),
    url("^stats/$",views.statsView,name = "stats"),
]
