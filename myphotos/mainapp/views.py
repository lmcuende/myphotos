from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from mainapp.models import Photo, Comment
from mainapp.forms import PhotoForm, CommentForm, ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage

def about(requets):
	html = '<html><body>App for upload and comment photos to a blog</body></html>'
	return HttpResponse(html)

def home(request):
	photos = Photo.objects.all()
	return render_to_response('home.html',{'photos':photos}, context_instance=RequestContext(request))

def users(request):
	users = User.objects.all()
	photos = Photo.objects.all()
	return render_to_response('users.html',{'users':users,'photos':photos}, context_instance=RequestContext(request))

def list_photos(request):
	photos = Photo.objects.all()
	return render_to_response('photos.html',{'data':photos}, context_instance=RequestContext(request))

def photo_detail(request, id_photo):
	datum = get_object_or_404(Photo, pk=id_photo)
	comments = Comment.objects.filter(photo=datum)
	return render_to_response('photo.html',{'photo':datum,'comments':comments},context_instance=RequestContext(request))

def new_photo(request):
	form = PhotoForm()
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/photos')
	else:
		form = PhotoForm()
	return render_to_response('photoform.html',{'form':form}, context_instance=RequestContext(request))

def new_comment(request):
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/photos')
	else:
		form = CommentForm()
	return render_to_response('commentform.html',{'form':form}, context_instance=RequestContext(request))


def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			subject = 'Message from MyPhotos'
			content = form.cleaned_data['message'] + "\n"
			content += 'Reply to: ' + form.cleaned_data['mail']
			mail = EmailMessage(subject, content, to=['lm@cuende.pro'])
			mail.send()
			return HttpResponseRedirect('/')
	else:
		form = ContactForm()
	return render_to_response('contactform.html',{'form':form}, context_instance=RequestContext(request))
