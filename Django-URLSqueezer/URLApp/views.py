from django.shortcuts import render, get_object_or_404, redirect
from .models import Shrink


def show_url(request, short_url):
    short_url = get_object_or_404(Shrink, short_url=short_url)
    return render(request, 'URLApp/urls_base.html', {'url': short_url})


def urls_base(request):
    if request.method == "POST":
        shrink = Shrink()
        shrink.long_url = request.POST.get('input_url')

        short_temp_url = 'jhdslfs'
        shrink.short_url = short_temp_url
        shrink.save()

        # url_input = request.POST['url']
        # url_input = Shrink(long_url=url_input, short_url=shorten_alg(url_input))

        return redirect('show_url', shrink.short_url)
        # return render(request, 'URLApp/url_output.html', {"short_url": shrink.short_url})
    return render(request, 'URLApp/urls_base.html')


# def shorten_alg():
    # given a long, return a short
