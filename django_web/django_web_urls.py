from django.contrib import admin
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('v1/',views.v1),
    re_path('v2_exp/',views.v2_exp),
    re_path('v3/',views.v3),
    re_path('v4/',views.v4),
    re_path('v5/',views.v5),
    re_path('v6/',views.v7),
    re_path('v7/',views.v6),


]
