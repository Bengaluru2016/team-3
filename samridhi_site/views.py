from django.shortcuts import render
import requests

from settings import sid, token

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
