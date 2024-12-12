from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('spso/', views.spso_home, name='spso_home'),
    path('spso/add_printer/', views.spso_add_printer, name='spso_add_printer'),
    path('spso/edit_printer/<int:pk>/', views.spso_config_printer, name='spso_edit_printer'),
    path('spso/delete_printer/<int:pk>/', views.spso_delete_printer, name='spso_delete_printer'),
    path('spso/printer_list/', views.spso_printer_list, name='spso_printer_list'),
    path('spso/logs/', views.spso_logs, name='spso_logs'),
    path('spso/view_report/', views.spso_view_report, name='spso_view_report'),
    path('spso/printing_services_config/',
         views.spso_printing_services_config, name='spso_printing_services_config'),

    path('<str:pk>/', views.student_home, name='student_home'),
    path('<str:pk>/printing_services/', views.student_printing_services, name='student_printing_services'),
    path('<str:pk>/buy_pages/', views.student_buy_pages, name='student_buy_pages'),
    path('<str:pk>/logs/', views.student_logs, name='student_logs'),
]
