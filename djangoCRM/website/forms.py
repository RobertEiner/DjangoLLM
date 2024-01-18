from django import forms
from django.forms import ModelForm
from .models import Record, Item


class RecordForm(ModelForm):
    # The tutorial guy doesn't really know what meta is, but it's necessary
    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'address', 'city')
        labels =  {
            'First name': '',
            'Last name': '',
            'Address': '',
            'City': ''
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
         }
        
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'price', 'name', 'color', 'image')
        labels = {
            'Category': '',
            'Price': '',
            'Name': '',
            'Color': '',
            'Image': ''
        }
        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control', 'placeholder':'category'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'price'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color'}),
         }
        
# class LLMInputForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = ('input',)
#         labels = {
#             'input': ''
#         }
       
        

        


