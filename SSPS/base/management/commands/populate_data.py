from django.core.management.base import BaseCommand
from base.models import Printer, PrintJob, Student
from django.utils import timezone
import random
from datetime import timedelta
from .generate_val import students, printers, document_names


class Command(BaseCommand):
    help = 'Populate the database with sample Printer, Student and PrintJob data.'

    def handle(self, *args, **kwargs):
        student_ids = [student.student_id for student in students]
        printer_ids = list(range(1, 21))
        current_time = timezone.now()
        page_sizes_choices = ['A4', 'Letter', 'A3', 'A5', 'Legal']

        print_jobs = []
        for _ in range(1, 501):
            student_id = random.choice(student_ids)
            printer_id = random.choice(printer_ids)
            start = current_time - timedelta(days=random.randint(1, 30), hours=random.randint(0, 23))
            end = start + timedelta(minutes=random.randint(5, 120))

            num_pages = random.randint(1, 100)
            file_name = random.choice(document_names)
            no_copies = random.randint(1, 10)
            page_sizes = random.choice(page_sizes_choices)
            one_sided = random.choice([True, False])

            print_jobs.append(PrintJob(
                student_id=student_id,
                printer_id=printer_id,
                start_time=start,
                end_time=end,
                num_pages=num_pages,
                file_name=file_name,
                no_copies=no_copies,
                page_sizes=page_sizes,
                one_sided=one_sided
            ))

        Student.objects.bulk_create(students)
        Printer.objects.bulk_create(printers)
        self.stdout.write(self.style.SUCCESS('Successfully created Students and Printers'))

        PrintJob.objects.bulk_create(print_jobs)
        self.stdout.write(self.style.SUCCESS('Successfully created PrintJobs'))
