from django.urls import path
from .views import todoview,addtask, deletetask, edittaskview, edit

urlpatterns = [
    path('',todoview, name = 'homepage'),
    path('addtask/',addtask, name = 'addtask'),
    path('delete/<int:taskpk>/', deletetask, name = 'deletetask'),
    path('edittask/<int:taskpk>/', edittaskview, name='edittask'),
    path('edittask/<int:taskpk>/update/',edit, name = 'edit')
]
