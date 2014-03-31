from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from mainapp.models import Photo, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def about(requets):
	html = '<html><body>App for upload and comment photos to a blog</body></html>'
	return HttpResponse(html)

def home(request):
	photos = Photo.objects.all()
	return render_to_response('home.html',{'photos':photos})

def users(request):
	users = User.objects.all()
	photos = Photo.objects.all()
	return render_to_response('users.html',{'users':users,'photos':photos})

def list_photos(request):
	photos = Photo.objects.all()
	return render_to_response('photos.html',{'data':photos}, context_instance=RequestContext(request))

def photo_detail(request, id_photo):
	datum = get_object_or_404(Photo, pk=id_photo)
	comments = Comment.objects.filter(photo=datum)
	return render_to_response('photo.html',{'photo':datum,'comments':comments},context_instance=RequestContext(request))

# Create your views here.
