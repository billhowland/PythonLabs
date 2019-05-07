from django.shortcuts import render, get_object_or_404, redirect
from .models import Shrink


def url_shrink(request):
    if request.method == "POST":
        url_input = request.POST['url']
        url_input = Shrink(long_url=url_input, short_url=shorten_alg(url_input))
        return render(request, 'short_url', pk=url_input.pk)
    else:
        return render()


def show_url(request, short_url):
    short_url = get_object_or_404(Shrink, short_url=short_url)
    return redirect("show_url", pk=short_url.pk)


# def shorten_alg():
    # given a long, return a short
