from django.urls import path
from . import views
#its a list of urls imported from the views file in the same directory

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('signup_p',views.signup_p,name="signup_p"),
    path('signup_c',views.signup_c,name="signup_c"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout")
]