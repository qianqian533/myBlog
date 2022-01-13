from django.shortcuts import render
from  . models import BlogPost,Entry
from . forms import BlogForm,EntryForm
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
	"""学习笔记的主页"""
	return render(request,'blogs/index.html')
	
@login_required	
def blogs(request):
	blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
	context = {'blogs':blogs}
	return render(request,'blogs/blogs.html',context)

@login_required	
def blog(request,blog_id):
	""""显示所有主题的条目"""
	blog=BlogPost.objects.get(id=blog_id)
	if blog.owner != request.user:
		raise Http404
	entries = blog.entry_set.order_by('-date_added')
	context = {'blog':blog,'entries':entries}
	
	return render(request,'blogs/blog.html',context)

@login_required	
def new_blog(request):
	"""add new blog"""
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = BlogForm()
	else:
		#POST提交的数据。对数据进行处理
		form = BlogForm(request.POST)
		if form.is_valid():
			#form.instance.owner=request.user
			new_blog = form.save(commit=False)
			new_blog.owner = request.user
			new_blog.save()
			return HttpResponseRedirect(reverse('blogs:blogs'))
			
	context = {'form': form}
	return render(request, 'blogs/new_blog.html',context)	
	
@login_required	
def new_entry(request,blog_id):
	"""添加新主题"""
	blog = BlogPost.objects.get(id = blog_id)
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = EntryForm()
	else:
		#POST提交的数据。对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.blog = blog
			new_entry.save()
			return HttpResponseRedirect(reverse('blogs:blog',args=[blog_id]))
			
	context = {'blog':blog,'form': form}
	return render(request, 'blogs/new_entry.html',context)

@login_required	
def edit_entry(request,entry_id):
	"""添加新主题"""
	entry= Entry.objects.get(id = entry_id)
	blog = entry.blog
	if blog.owner != request.user:
		raise Http404
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = EntryForm(instance=entry)
	else:
		#POST提交的数据。对数据进行处理
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:blog',args=[blog.id]))
			
	context = {'entry':entry, 'blog':blog,'form': form}
	return render(request, 'blogs/edit_entry.html',context)
		
# Create your views here.
