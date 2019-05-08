from django.shortcuts import render, get_object_or_404, redirect
from .models import Shrink


def show_url(request, short_url):
    url = get_object_or_404(Shrink, short_url=short_url)
    if url.long_url.startswith('http'):
        return redirect(url.long_url)
    else:
        return redirect('http://' + url.long_url)


def urls_base(request):
    if request.method == "POST":
        url_input = request.POST['input_url']
        if not Shrink.objects.filter(long_url=url_input).exists():
            shrink = Shrink(long_url=url_input, short_url=shorten_alg())
            shrink.save()
        else:
            shrink = Shrink.objects.get(long_url=url_input)
        return render(request, 'URLApp/urls_base.html', {'url': shrink})

        # return render(request, 'URLApp/url_output.html', {"short_url": shrink.short_url})
    return render(request, 'URLApp/urls_base.html')


def shorten_alg():
    # given a long, return a short
    import random
    seed = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?')
    a = 0
    rand_url = ''

    while a < 10:
        seed_var = random.choice(seed)
        rand_url += seed_var
        a += 1
        continue
    return(rand_url)
