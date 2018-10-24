from django.conf.urls import url
from . import views

# eg:url(r'^book/$',views.BookView.as_view()),
urlpatterns = [
    url(r'sms_code/(?P<mobile>1[3-9]\d{9})/$',views.SMSCodeView.as_view())
]
