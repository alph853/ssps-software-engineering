from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),

    path('<str:pk>/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('<str:pk>/printing_services/', views.student_printing_services, name='student_printing_services'),
    path('<str:pk>/buy_pages/', views.student_buy_pages, name='student_buy_pages'),
    path('<str:pk>/student_logs/', views.student_logs, name='student_logs'),

    path('spso/dashboard/', views.spso_dashboard, name='spso_dashboard'),
    path('spso/add_printer/', views.spso_add_printer, name='spso_add_printer'),
    path('spso/edit_printer/<int:pk>', views.spso_config_printer, name='spso_edit_printer'),
    path('spso/delete_printer/<int:pk>', views.spso_delete_printer, name='spso_delete_printer'),
    path('spso/printer_list', views.spso_printer_list, name='spso_printer_list'),
    path('spso/logs/', views.spso_logs, name='spso_logs'),
    # path('spso/view_report/', views.spso_view_report, name='spso_view_report'), 
    path('spso/config_service/', views.spso_config_service, name='spso_config_service'),
]
