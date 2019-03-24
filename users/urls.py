from django.urls import include, path

from users import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/school/', views.SchoolSignUpView.as_view(), name='school_signup'),
]