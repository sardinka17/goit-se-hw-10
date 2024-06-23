from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


from users.forms import LoginForm
from users.views import SignUpView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='users/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
