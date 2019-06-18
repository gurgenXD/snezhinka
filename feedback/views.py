from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from feedback.forms import CallBackForm, FeedBackForm
from landing.models import MailToString


class CallBackView(View):
    def post(self, request):
        callback_form = CallBackForm(request.POST)

        if callback_form.is_valid():
            try:
                current_site = get_current_site(request)
                mail_subject = 'Новый звонок на сайте: ' + current_site.domain
                message = render_to_string('feedback/callback_message.html', {
                    'domain': current_site.domain,
                    'phone': request.POST.get('phone'),
                })
                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
            except:
                sended = 0  #Письмо не отправлено
            else:
                callback_form.save()
                sended = 1  #Письмо отправлено
        else:
            sended = None

        context = {
            'sended': sended,
        }

        return JsonResponse(context)


class FeedBackView(View):
    def post(self, request):
        feedback_form = FeedBackForm(request.user, request.POST)

        if feedback_form.is_valid():
            if request.recaptcha_is_valid:
                try:
                    current_site = get_current_site(request)
                    mail_subject = 'Новое сообщение на сайте: ' + current_site.domain
                    message = render_to_string('feedback/feedback_message.html', {
                        'domain': current_site.domain,
                        'email': request.POST.get('email'),
                        'name': request.POST.get('name'),
                        'message': request.POST.get('message'),
                    })
                    to_email = MailToString.objects.first().email
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                except:
                    sended = 0  #Письмо не отправлено
                else:
                    feedback_form.save()
                    sended = 1  #Письмо отправлено
            else:
                sended = 3 #Рекапча неверная
        else:
            sended = None
            
        context = {
            'sended': sended,
        }

        return JsonResponse(context)

