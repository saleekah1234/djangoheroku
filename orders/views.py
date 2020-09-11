from django.shortcuts import render,redirect
from .models import Order
from .forms import OrderForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template


def viewhygio(request):
    form=OrderForm(request.POST or None)
    if form.is_valid():
        order=form.save(commit=False)
        order.save()
        ctx={'form':form}
        message = get_template('orders/mail.html').render(ctx)
        msg = EmailMessage(
        'New Order',
        message,
        'nastradelinksmkd@gmail.com',
        ['nastradelinksmkd@gmail.com'])
        msg.content_subtype = "html"
        msg.send()
    return render(request,'orders/index.html',{'form':form})


# Create your views here.
