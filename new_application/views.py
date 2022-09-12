from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import BankAccountApplicationForm
from django.http import HttpResponseRedirect,HttpResponse


def new_application(request):
    # POST REQUEST -- > CONTENTS --> APPROVED
    if request.method == "POST":
        form = BankAccountApplicationForm(request.POST)
        
        # VALIDATE ROUTINE::
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('account_application_form:approved', args=[form.instance.id]))
           
    # ELSE, Re-RENDER FORM    
    else:
        form = BankAccountApplicationForm
    return render(request, 'new_application/welcome.html', context={'form':form})

def approved(request, pk):
    approved_user = models.User.objects.get(pk=pk)
    return render(request, 'new_application/approved.html', context= {'approved_user':approved_user})