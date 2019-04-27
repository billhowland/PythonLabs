from django.shortcuts import render

# Create your views here.


def url_shortener(request):
    return render(request, 'urlslab/url_shortener.html', {})
