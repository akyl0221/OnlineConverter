from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

from youtube_converter.models import Download
from youtube_converter.forms import UrlForm
from youtube_converter.downloader import convert


def history(request):
    urls = Download.objects.all()
    return render(request, "history.html", {"urls": urls})


def converter(request):
    urlform = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            video_url = convert(url)
            Download.objects.create(url=url)
            return HttpResponsePermanentRedirect(video_url)
        return render(request, "home.html", {"form": urlform})
    else:
        return render(request, "home.html", {"form": urlform})
