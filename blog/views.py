from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Article

def home(request):
	article_list = Article.objects.all()
	return render(request,'home.html', { 'article_list': article_list })
