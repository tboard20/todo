from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('/dashboard',views.task_list,name="task_list"),
    path('index/',views.index,name="index"),
    # path('login/',views.login,name="login"),
    # path('logout/',views.logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('task/new/',views.task_create,name="task_create"),
    path('task/delete/<int:task_id>/',views.task_delete, name="task_delete"),
]