from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm
# from django.http import HttpResponse
# Create your views here.

# return render(request, 'meetups\index.html')


def index(request):
    # return HttpResponse("Hello World!")
    meetups = Meetup.objects.all()
    # [
    #     {'title': "My first Meetup", "location": "New York", "slug": "a-first-meetup"},
    #     {'title': "My second Meetup", "location": "paris", "slug": "a-second-meetup"}

    # ]
    return render(request, 'meetups/index.html', {
        # "show_meetups": True,
        "meetups": meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            registeration_from = RegistrationForm()

        else:
            registeration_from = RegistrationForm(request.POST)
            if registeration_from.is_valid():
                user_email = registeration_from.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(
                    email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm_registration', meetup_slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            "meetup_found": True,
            "meetup": selected_meetup,
            'form': registeration_from
        })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            "meetup_found": False,
        })


def confirm_registration(request, meetup_slug):
    meetup=Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html',{
        "organizer_email":meetup.organizer_email
        })
