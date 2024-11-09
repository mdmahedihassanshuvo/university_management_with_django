from celery import shared_task
from datetime import date
from .models import AcademicSemester


@shared_task
def create_semester_task():
    current_year = date.today().year
    semester_start_months = ['January', 'July']
    semester_names = {
        "January": f"Spring {current_year}",
        "July": f"Fall {current_year}",
    }

    for month in semester_start_months:
        if month == 'January':
            start_date = date(current_year, 1, 1)
            end_month = date(current_year, 6, 30)
        elif month == 'July':
            start_date = date(current_year, 7, 1)
            end_month = date(current_year, 12, 31)

        semester = AcademicSemester(
            name=semester_names[month],
            year=str(current_year),
            code=str(len(semester_start_months)),
            start_month=start_date,
            end_month=end_month
        )

        semester.save()
