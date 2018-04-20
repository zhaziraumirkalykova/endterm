from django.shortcuts import render

from api.models import Blog, Text


def index(request):
  return render(request, 'index.html')


def blog_list(request):
  blogs = Blog.objects.all().order_by('-created_at')
  return render(request, 'blog/blog_list.html', {"blog_list": blogs, "active_menu": "blog"})


def blog_detail(request, blog_id):
  blog = Blog.objects.get(pk=blog_id)
  return render(request, 'blog/blog_detail.html', {"blog": blog, "active_menu": "blog"})


def text_list(request):
  texts = Text.objects.all()
  return render(request, 'text/text_list.html', {"text_list": texts, "active_menu": "text"})

def text_detail(request,text_id):
	text = Text.objects.get(pk=text_id)
	return render(request, 'text/text_detail.html', {"text" : text, "activate_menu" : "text"}) 