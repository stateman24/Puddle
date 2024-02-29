from django.urls import path
from .views import index, contact, signup, signout, category
from .forms import LoginForm
from django.contrib.auth import views as auth_views 


app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/', category, name='category'),
    path("signup/", signup,  name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', signout, name='logout')
]
