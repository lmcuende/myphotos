#encoding:utf-8
from django.forms import ModelForm
from django import forms
from mainapp.models import Photo, Comment

class PhotoForm(ModelForm):
	class Meta:
		model = Photo

class CommentForm(ModelForm):
	class Meta:
		model = Comment

class ContactForm(forms.Form):
	mail = forms.EmailField(label='Your email')
	message = forms.CharField(widget=forms.Textarea)