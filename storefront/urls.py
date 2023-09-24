"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import *  # Import only what's needed

urlpatterns =[

    path('admin/', admin.site.urls),
    path("", include('yogi.urls')),
    path("receipe/", receipes, name="receipes"),
    path("delete_receipe/<id>/",delete_receipe,name="delete-receipe"),
    path("update_receipe/<id>/",updating,name="update-receipe"),
    path("login_page/",login_page,name="login_page"),
    path("register_page/",register_page,name="register_page"),
    path("log_out/",log_out,name="log_out"),
    path("cards/",report_card,name="cards"),
    path("marks_student/<student_id>",marks_of_student,name="marks"),
    path("send_mails/<student_id>/<student_email>/<father_email>",sending,name="emails"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()