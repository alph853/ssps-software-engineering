from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=7, unique=True, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    page_balance = models.IntegerField(default=200)

    def __str__(self):
        return f'{self.lname} {self.fname} ({self.student_id})'


PrinterStatus = [
    ('Đang hoạt động', 'Đang hoạt động'),
    ('Vô hiệu hóa', 'Vô hiệu hóa'),
    ('Gặp sự cố', 'Gặp sự cố'),
    ('Hàng đợi đầy', 'Hàng đợi đầy')
]

Campus = [
    ('Lý Thường Kiệt', 'Lý Thường Kiệt'),
    ('Dĩ An', 'Dĩ An')
]

PageSize = [
    ('A4', 'A4'),
    ('Letter', 'Letter'),
    ('A3', 'A3'),
    ('A5', 'A5'),
    ('Legal', 'Legal')
]


class Printer(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    building = models.CharField(max_length=10)
    room = models.CharField(max_length=100)
    campus = models.CharField(
        max_length=50,
        choices=Campus,
    )
    status = models.CharField(
        max_length=20,
        choices=PrinterStatus,
        default=('enabled', 'Enabled')
    )
    total_pages_used = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.building} - {self.room}) {self.brand} {self.model}"


class PrintJob(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='print_logs')
    printer = models.ForeignKey('Printer', on_delete=models.CASCADE, related_name='print_logs')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)

    num_pages = models.IntegerField()
    file_name = models.CharField(max_length=255)
    no_copies = models.IntegerField()
    page_sizes = models.CharField(
        max_length=20,
        choices=PageSize,
    )
    one_sided = models.BooleanField()

    def __str__(self):
        return f'{self.student} starts {self.file_name} on {self.printer} at {self.start_time}'
