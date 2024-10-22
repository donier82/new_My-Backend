from django.http import HttpRequest
from django.shortcuts import render
from apps.settings.models import Settings, Shape, About, Contact
from django.core.mail import send_mail
from apps.settings.utils import send_contact_email

# Create your views here.
def index(request: HttpRequest):
    settings_id = Settings.objects.latest('id')
    shape_all = Shape.objects.all()
    about_id = About.objects.latest('id')
    #contact=Contact.objects.latest('id')

    if request.method == 'POST':
        name = request.POST.get('inputName')
        email = request.POST.get('inputEmail')
        phone = request.POST.get('inputPhone')
        subject = request.POST.get('inputSubject')
        message = request.POST.get('inputMessage')
 
        send_mail(
            'Pet Project',
            f"""
            Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            name :{name}
            email : {email}
            phone : {phone}
            subject : {subject}
            message : {message}

            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными
            данными! """,
            "noreply@somehost.local",
            ["donierosh@gmail.com"],
            fail_silently = False
        )
        send_contact_email.delay(name, email, phone, subject, message)

    return render(request, 'index.html', locals())