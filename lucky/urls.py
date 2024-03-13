from lucky import views
from django.urls import path

urlpatterns = [



    path("",views.homepage),
    path("aboutus",views.aboutus),
    path("contactus",views.contactusx,name="contactus"),
    path("services",views.services,name="services"),

    path("signup",views.signup, name="signup"),

    path("login",views.mylogin, name="login"),
    
    path("logout",views.mylogout,name="logout"),


    
    path("datasave",views.savethis),


    path("delete-this/<int:dfg>",views.deletethisdata),


    path("update-this/<int:zxc>",views.updatethisdata),

    
    path("now-updatethis/<int:updateid>",views.nowupdatedata),
    
    path("search",views.searchthisdata,name="mysearch")

]
