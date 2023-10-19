from django.urls import path

from backend import views



urlpatterns= [

    path('Dept/',views.Dept,name="Dept"),
    path('indexpage/',views.indexpage,name="indexpage"),
    path('savedept/',views.savedept,name="savedept"),
    path('Deptdisplay/',views.Deptdisplay,name="Deptdisplay"),
    path('editdept/<int:dataid>/',views.editdept,name="editdept"),
    path('updatedept/<int:dataid>/',views.updatedept,name="updatedept"),
    path('deletedept/<int:dataid>/',views.deletedept,name="deletedept"),
    path('adddoc/',views.adddoc,name="adddoc"),
    path('savedoc/',views.savedoc,name="savedoc"),
    path('displaydoc/',views.displaydoc,name="displaydoc"),
    path('editdoc/<int:docid>/',views.editdoc,name="editdoc"),
    path('deldoc/<int:docid>/',views.deldoc,name="deldoc"),
    path('updatedoc/<int:docid>/',views.updatedoc,name="updatedoc"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('bookingpage/',views.bookingpage,name="bookingpage"),


    




]