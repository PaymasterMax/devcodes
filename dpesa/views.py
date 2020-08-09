from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from django.urls import reverse

def index(request):
    cl = MpesaClient()
    phone_number = '254797494509'
    amount = 1
    account_reference = '10367'
    transaction_desc = 'Description'
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    print(callback_url)
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response.response_description)

def stk_push_callback(request):
        data = request.body
