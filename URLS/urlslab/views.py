from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def url_shortener(request):
    if POST:
        url_input = req.POST['url']
        url = URL(long=url_input,
                  short=shorten_alg(url_in))
        url.save()
        redirect('show_url', {long: long})


def redirect(reg, short_url):
    url = get_object_or_404(URL, short=short_url)
    redirect(url.long)


def index(reg):
