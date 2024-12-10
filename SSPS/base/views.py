from django.shortcuts import redirect, render, HttpResponse
from .models import Printer, PrinterStatus, PrintJob, Student
from .forms import PrintJobForm, PrinterForm
# Create your views here.


allowed_file_ext_choices = ['pdf', 'jpg', 'png', 'txt', 'jpeg']
page_sizes_choices = ['A4', 'Letter', 'A3', 'A5', 'Legal']
default_page_num = 200
reset_date = ['start of semester', 'end of semester', 'middle of semester']


def login(request):
    return render(request, 'base/login.html')

def student_dashboard(request):
    return render(request, 'base/home.html')


def student_printing_services(request):
    if request.method == 'POST':
        form = PrintJobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/student_logs')
    else:
        form = PrintJobForm()
    context = {'form': form}
    return render(request, 'base/printjob_form.html', context)


def student_buy_pages(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.pages_left += default_page_num
        student.save()
        return redirect('/student_dashboard')
    return render(request, 'base/buy_more_pages.html')


def student_logs(request):
    logs = PrintJob.objects.all()
    return render(request, 'base/student_logs.html')


def spso_dashboard(request):
    return render(request, 'base/home.html')


def spso_add_printer(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/spso/printer_list')
    else:
        form = PrinterForm()
    context = {'form': form}
    return render(request, 'base/printer_form.html', context)


def spso_printer_list(request):
    printers = Printer.objects.all()
    status_classes = list()
    for printer in printers:
        if printer.status == 'Đang hoạt động':
            status_classes.append('enabled')
        elif printer.status == 'Vô hiệu hóa':
            status_classes.append('disabled')
        elif printer.status == 'Gặp sự cố':
            status_classes.append('malfunction')
        else:
            status_classes.append('full')
    zipped = zip(printers, status_classes)
    context = {'printers': zipped}
    return render(request, 'base/view_printers.html', context)


def spso_config_printer(request, pk):
    printer = Printer.objects.get(pk=pk)
    if request.method == 'POST':
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            return redirect('/spso/printer_list')
    else:
        form = PrinterForm(instance=printer)
    context = {'form': form}
    return render(request, 'base/printer_form.html', context)


def spso_delete_printer(request, pk):
    printer = Printer.objects.get(pk=pk)
    printer.delete()
    return redirect('/spso/printer_list')

def spso_logs(request):
    logs = PrintJob.objects.all()
    context = {'logs': logs}
    return render(request, 'base/spso_logs.html', context)


def spso_config_service(request):
    if request.method == 'POST':
        page_size = request.POST['page_size']
        page_num = request.POST['page_num']
        reset_date = request.POST['reset_date']
        return HttpResponse(f'Page size: {page_size}, Page number: {page_num}, Reset date: {reset_date}')
    return render(request, 'base/config_service.html')