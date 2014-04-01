#encoding:utf-8
from django.forms import ModelForm
from django import forms
from mainapp.models import Photo, Comment

class ContactForm(forms.Form):
	mail = forms.EmailField(label='Your email')
	message = forms.CharField(widget=forms.Textarea)