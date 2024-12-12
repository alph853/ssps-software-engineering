import math
from PyPDF2 import PdfReader
import os
from django import forms
from .models import Printer, PrintJob, PrinterStatus, Campus, PageSize, Student


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'

    brand = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    model = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        }),
    )
    building = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    room = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        help_text=''
    )
    campus = forms.ChoiceField(
        choices=Campus,  # Assuming you have defined CAMPUS_CHOICES in Printer model
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )
    status = forms.ChoiceField(
        choices=PrinterStatus,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        initial=('Đang hoạt động', 'Đang hoạt động')
    )
    total_pages_used = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )


class PrintJobForm(forms.Form):
    printer = forms.ModelChoiceField(
        queryset=Printer.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/png, image/jpeg, image/jpg, application/pdf, text/plain'
        }),
        required=True,
    )
    no_copies = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Số bản sao in'
        }),
    )
    page_sizes = forms.ChoiceField(
        initial=('A4', 'A4'),
        choices=[
            ('A4', 'A4'),
            ('Letter', 'Letter'),
            ('A3', 'A3'),
            ('A5', 'A5'),
            ('Legal', 'Legal')
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
    )
    one_sided = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    def save(self, student_id):
        file_path = self.cleaned_data['file'].name
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.pdf':
            reader = PdfReader(self.cleaned_data['file'])
            num_pages = len(reader.pages)
        elif file_extension in ['.jpg', '.jpeg', '.png', '.txt']:
            num_pages = 1

        num_pages *= self.cleaned_data['no_copies']
        student = Student.objects.get(student_id=student_id)
        if student.page_balance < num_pages:
            return f'Số trang in ({num_pages}) vượt quá số trang còn lại ({student.page_balance}).'
        student.page_balance -= num_pages

        return PrintJob.objects.create(
            student_id=student_id,
            printer=self.cleaned_data['printer'],
            num_pages=num_pages,
            file_name=os.path.basename(self.cleaned_data['file'].name),
            no_copies=self.cleaned_data['no_copies'],
            page_sizes=self.cleaned_data['page_sizes'],
            one_sided=self.cleaned_data['one_sided']
        )

