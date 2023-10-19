from django.urls import path

from frontend import views

urlpatterns= [
    path('home/',views.home,name="home"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('servicepage/',views.servicepage,name="servicepage"),
    path('departmentpage/',views.departmentpage,name="departmentpage"),
    path('deptsingle/<int:dept_id>/',views.deptsingle,name="deptsingle"),
    path('doctorpage/',views.doctorpage,name="doctorpage"),
    path('docsingle/<int:doc_id>/',views.docsingle,name="docsingle"),
    path('regpage/',views.regpage,name="regpage"),
    path('savereg/',views.savereg,name="savereg"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('appointpage/',views.appointpage,name="appointpage"),
    path('saveappoint/',views.saveappoint,name="saveappoint"),
    path('confirmpage/',views.confirmpage,name="confirmpage"),
    path('contactpage/',views.contactpage,name="contactpage"),


]