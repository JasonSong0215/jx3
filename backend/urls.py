#Author:Jason Song
from django.conf.urls import url
from backend import jx3,test_dps,pwd

urlpatterns = [
    url(r'cal', jx3.cal,),
    url(r'authdps', jx3.auth,),
    url(r'test_dps', test_dps.test_dps,),
    url(r'pwd', pwd.pwd,),

]