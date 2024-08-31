from django.shortcuts import render
from django.conf import settings


def homepage(request):

    context = {
        "use_blog": settings.ENABLE_BLOG
    }
    return render(request , "index.html", context=context)