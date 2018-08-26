from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
#powyższe przygotowuje strone do wyświetlenia; post list jest kodem do przygotowania strony, ten post list przygotowujemy w HTMLu ze znacznikami Django (np. pozwalają wyświetlić kilka artykułów pisząc jedna komendę)
