from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
	
#powyższe przygotowuje strone do wyświetlenia; post list jest kodem do przygotowania strony, ten post list przygotowujemy w HTMLu ze znacznikami Django (np. pozwalają wyświetlić kilka artykułów pisząc jedna komendę)
