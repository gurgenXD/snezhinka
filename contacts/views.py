from django.shortcuts import render
from django.views import View
from contacts.models import Phone, Schedule, Address, Fax, Email, MapCode
from feedback.forms import FeedBackForm


class ContactView(View):
    def get(self, request):
        phones = Phone.objects.all()
        shedules = Schedule.objects.all()
        addresses = Address.objects.all()
        faxes = Fax.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()

        feedback_form = FeedBackForm(request.user)
        
        context = {
            'phones': phones,
            'shedules': shedules,
            'addresses': addresses,
            'faxes': faxes,
            'emails': emails,
            'map_code': map_code,
            'feedback_form': feedback_form,
        }

        return render(request, 'contacts/contacts.html', context)
