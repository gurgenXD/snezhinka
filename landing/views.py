from django.shortcuts import render
from django.views import View
from news.models import News
from contacts.models import Phone, Schedule, Address, Fax, Email, MapCode
from feedback.forms import FeedBackForm
from landing.models import Agreement


class IndexView(View):
    def get(self, request):
        news = News.objects.all()[:2]

        phones = Phone.objects.all()
        shedules = Schedule.objects.all()
        addresses = Address.objects.all()
        faxes = Fax.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()

        feedback_form = FeedBackForm(request.user)
        
        context = {
            'news': news,
            'phones': phones,
            'shedules': shedules,
            'addresses': addresses,
            'faxes': faxes,
            'emails': emails,
            'map_code': map_code,
            'feedback_form': feedback_form,
        }

        return render(request, 'landing/index.html', context)


class UsersContentView(View):
    def get(self, request):
        
        context = {
        }

        return render(request, 'landing/users_content.html', context)


class AgreementView(View):
    def get(self, request):
        agreement = Agreement.objects.first()
        
        context = {
            'agreement': agreement,
        }

        return render(request, 'landing/agreement.html', context)