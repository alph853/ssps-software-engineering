from django.shortcuts import redirect, render, HttpResponse
from .models import Printer, PrinterStatus, PrintJob, Student
from .forms import PrintJobForm, PrinterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
LOGIN = False
NUM_TRANSACTION = 0

allowed_file_ext_choices = ['pdf', 'jpg', 'png', 'txt', 'jpeg']
page_sizes_choices = ['A4', 'Letter', 'A3', 'A5', 'Legal']
default_page_num = 200
reset_date_options = ['start of semester', 'end of semester', 'middle of semester', 'start of month', 'end of month']
reset_date = 'start of semester'


def spso_printing_services_config(request):
    global allowed_file_ext_choices, page_sizes_choices, default_page_num, reset_date
    if request.method == 'POST':
        # allowed_file_ext_choices = request.POST.get('allowed_file_ext_choices')
        # page_sizes_choices = request.POST.get('page_sizes_choices')
        default_page_num = request.POST.get('default_page_num')
        reset_date = request.POST.get('reset_date')

    context = {
        'allowed_file_ext_choices': allowed_file_ext_choices,
        'page_sizes_choices': page_sizes_choices,
        'default_page_num': default_page_num,
        'reset_date_options': reset_date_options,
        'reset_date': reset_date
    }
    return render(request, 'base/spso_printing_services_config.html', context)


def home(request):
    context = {'login': False}
    return render(request, 'base/index.html', context)


def spso_home(request):
    context = {'login': True}
    return render(request, 'base/index.html', context)


def student_home(request, pk):
    context = {'login': True, 'student_id': pk}
    return render(request, 'base/index.html', context)


def login_page(request):
    if request.method == 'POST':
        global LOGIN

        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'spso' and password == 'hcmut123':
            LOGIN = True
            return redirect(f'/spso/')
        else:
            try:
                student = Student.objects.get(username=username, password=password)
                LOGIN = True
                return redirect('/' + student.student_id)
            except Student.DoesNotExist:
                messages.error(request, 'Người dùng không tồn tại.')
    # context = {'form': form}
    return render(request, 'base/login.html')


def logout_page(request):
    global LOGIN
    LOGIN = False
    global STUDENT_ID
    STUDENT_ID = None
    return redirect('/')


def student_printing_services(request, pk):
    if request.method == 'POST':
        form = PrintJobForm(request.POST, request.FILES)
        if form.is_valid():
            returned = form.save(pk)
            if isinstance(returned, PrintJob):
                messages.success(request, 'Gửi yêu cầu in thành công.')
            else:
                messages.error(request, returned)
        else:
            messages.error(request, 'Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin đã nhập.')
    else:
        form = PrintJobForm()
    context = {'form': form, 'student_id': pk}
    return render(request, 'base/printjob_form.html', context)


def student_buy_pages(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.page_balance += int(request.POST.get('pages'))
        global NUM_TRANSACTION
        NUM_TRANSACTION += 1
        student.save()
        messages.success(request, 'Mua giấy thành công.')
    page_balance = student.page_balance
    context = {'page_balance': page_balance, 'student_id': pk}
    return render(request, 'base/buy_more_pages.html', context)


def student_logs(request, pk):
    logs = PrintJob.objects.filter(student_id=pk)
    context = {'logs': logs, 'student_id': pk}
    return render(request, 'base/student_logs.html', context)


def spso_add_printer(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm máy in thành công.')
        else:
            messages.error(request, 'Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin đã nhập.')
    else:
        form = PrinterForm()
    context = {'form': form, 'title': 'Thêm máy in'}
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
            messages.success(request, 'Cập nhật máy in thành công.')
        else:
            messages.error(request, 'Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin đã nhập.')
    else:
        form = PrinterForm(instance=printer)
    context = {'form': form, 'title': 'Chỉnh sửa máy in'}
    return render(request, 'base/printer_form.html', context)


def spso_delete_printer(request, pk):
    printer = Printer.objects.get(pk=pk)
    if request.method == 'POST':
        printer.delete()
        return redirect('/spso/printer_list/')
    context = {'printer': printer}
    return render(request, 'base/delete_printer_form.html', context)

def spso_logs(request):
    logs = PrintJob.objects.all()
    context = {'logs': logs}
    return render(request, 'base/spso_logs.html', context)


def spso_view_report(request):
    printjobs = PrintJob.objects.all()
    total_paper = sum([job.num_pages for job in printjobs])
    total_print = len(printjobs)
    total_transaction = NUM_TRANSACTION
    context = {'total_paper': total_paper, 'total_print': total_print, 'total_transaction': total_transaction}
    return render(request, 'base/spso_view_report.html', context)
