from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.db import Q

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    try:
        overdue_loan = None
        current_date = timezone.now().date()
        overdue_loan = Loan.objects.filter(
            Q(is_returned=False) | Q(return_date>current_date)
        ).values()
        if overdue_loan is not None:
            send_mail(
                subject='Book Loaned Overdue',
                message=f'Hello {loan.member.user.username},\n\nYou have an overdue loan for the book "{book_title}".\nPlease return it urgently.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[member_email],
                fail_silently=False,
            )
    except Loan.DoesNotExist:
        pass
        