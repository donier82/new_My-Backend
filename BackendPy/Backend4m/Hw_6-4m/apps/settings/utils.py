from celery import shared_task
from django.core.mail import send_mail
from apps.settings.models import Contact

@shared_task
def send_contact_email(name, email, phone, subject, message):
    Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)