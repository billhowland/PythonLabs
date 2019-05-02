from django.shortcuts import redirect
from .models import Url
from .models import Task
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import TaskForm
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required

# from .forms import TaskForm

# Create your views here.


def url_shortener(request):
    if POST:
        url_input = req.POST['url']
        url = URL(long=url_input,
                  short=shorten_alg(url_in))
        url.save()
        redirect('show_url', {long: long})


def re_direct(reg, short_url):
    url = get_object_or_404(URL, short=short_url)
    redirect(url.long)


# def index(reg):
