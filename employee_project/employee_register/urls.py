from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.employeeForm, name='employee_insert'),
    path('<int:id>/', views.employeeForm, name="employee_update"),
    path('list/', views.employeeList, name= "employee_list"),
    path('form/', views.employeeForm ),
    path('delete/<int:id>', views.employeeDelete, name='employee_delete')
   
]