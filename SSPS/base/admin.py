from django.contrib import admin

# Register your models here.

from .models import Student, PrintJob, Printer

admin.site.register(Student)
admin.site.register(Printer)
admin.site.register(PrintJob)
