from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('todo/', views.todo, name='todo'),
    path('add/',views.add,name='add'),
    path("delete/<str:str>",views.delete, name="delete"),
    path('edit/<str:str>',views.edit,name='edit'),
    path('search/<str:str>/',views.search,name='search') 
]