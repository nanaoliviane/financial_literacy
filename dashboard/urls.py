from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('add_budget/', views.add_budget, name='add_budget'),
    path('budget_list/', views.budget_list, name='budget_list'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('goal_list/', views.goal_list, name='goal_list'),
]
