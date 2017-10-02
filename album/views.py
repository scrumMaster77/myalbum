# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
# Create your views here.


def base(request):
	return render(request, 'base.html')


class PhotoListView(ListView):
	"""docstring for ClassName"""
	model = Photo

class PhotoDetailView(DetailView):
	"""docstring for ClassName"""
	model = Photo	

class PhotoUpdate(UpdateView):
	"""docstring for PhotoUpdate"""
	model = Photo
	fields = '__all__'

class PhotoCreate(CreateView):
	"""docstring for ClassName"""
	model = Photo
	fields = '__all__'

class PhotoDelete(DeleteView):
	"""docstring for ClassName"""
	model = Photo
	success_url = reverse_lazy('photo-list')			


#def first_view(request):
#	return HttpResponse('Esta es mi primera vista!')

def category(request):
	category_list = Category.objects.all()
	context = {'object_list': category_list}
	return render(request, 'album/category.html',context)

def category_detail(request, category_id):

	category = Category.objects.get(id=category_id)
	context = { 'object' : category}
	return render(request, 'album/category_detail.html',context)

def photo_detail(request, photo_id):

	photo = Photo.objects.get(id=photo_id)
	context = { 'object' : photo}
	return render(request, 'album/photo_detail.html',context)