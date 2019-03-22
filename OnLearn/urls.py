

from django.contrib import admin

from django.conf.urls import url

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]
