from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Record, Item
from .forms import RecordForm, ItemForm
from django.shortcuts import get_object_or_404
from langchain import HuggingFaceHub
from huggingface_hub import InferenceClient
import os


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def add_record(request):
    submitted = False
    if request.method == 'POST': # if the request is a POST-method,
        form = RecordForm(request.POST) # then take the request and pass it to the form we created in forms.py (RecordForm)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect('/add_record?submitted=True')
    else:
        form = RecordForm() # Clear the form if a GET request is coming in 
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_record.html', { 'recordForm': form, 'submitted': submitted })

def add_item(request):
    submitted = False
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form.save()
            return HttpResponseRedirect('/add_item?submitted=True')
    else:
        item_form = ItemForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_item.html', {'itemForm': item_form, 'submitted': submitted})


def show_records(request):
    all_records = Record.objects.all()
    return render(request, 'show_records.html', {'records': all_records})


def show_items(request):
    if request.GET.get('item_id'):
        print('ITEM ID')
        item_id = request.GET.get('item_id')
        print(item_id)
        instance = get_object_or_404(Item, id=item_id)
        if(instance):
            instance.delete()
        print(instance)
    all_items = Item.objects.all()
   
    return render(request, 'show_items.html', { 'items': all_items })


def llm(request):
    response = ''
    if request.GET.get('generate') and request.GET.get('input'):
        prompt = request.GET.get('input')
        print(prompt)
        model_id = "tiiuae/falcon-7b-instruct"
        falcon_llm = HuggingFaceHub(
            repo_id=model_id,
            model_kwargs={"temperature":0.9, "max_new_tokens":2000},
            huggingfacehub_api_token='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'
        )

        response = falcon_llm(prompt)
        print(response)
    return render(request, 'llm.html', { 'response': response })

def llm2(request):
    response2 = ''
    if request.GET.get('generate') and request.GET.get('input'):
        prompt = request.GET.get('input')
        print(prompt)
        model_id = "tiiuae/falcon-7b-instruct"
        falcon_llm = HuggingFaceHub(
            repo_id=model_id,
            model_kwargs={"temperature":0.1, "max_new_tokens":2000},
            huggingfacehub_api_token='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'
        )

        response2 = falcon_llm(prompt)
        print(response2)
    return render(request, 'llm2.html', { 'response2': response2 })
    

def createRecord(request):
    pass

def delete_item():
    pass

