from django.shortcuts import render
import requests
from .forms import BaselineForm, HealthForms
from django.shortcuts import redirect

def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        })

def index_page(request):
    return render(request, 'samridhi_site/index.html', {})

def notify_person(request):
    sid = 'none585'
    token = '0e7d6190249459c6d9ab400447a03ab4241537a8'
    sms_body= 'These people are not attending classes for more than 3 days'
    send_message(sid, token, '9482582204', '9482582203', sms_body)

def survey(request):
    form = BaselineForm()
    if request.method == 'POST':
        form = BaselineForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'samridhi_site/index.html', {})
    return render(request, 'samridhi_site/survey.html', {'form':form})

def health(request):
    form = HealthForms()
    if request.method == 'POST':
        form = HealthForms(request.POST)
        print (form.is_valid())
        print (form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'samridhi_site/index.html', {})
    return render(request, 'samridhi_site/health.html', {'form':form})

def attendance(request):
    form = HealthForms()
    if request.method == 'POST':
        form = HealthForms(request.POST)
        print (form.is_valid())
        print (form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'samridhi_site/index.html', {})
    return render(request, 'samridhi_site/attendance.html', {'form':form})
