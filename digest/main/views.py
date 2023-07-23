from django.http import HttpResponse
from django.shortcuts import render
from .rss_parser import *
import json


def index(request):
    return render(request, 'main/index.html')


def get_digest(request):
    user_id = request.POST.get("user_id")
    digest = pull_feed(user_id)
    return HttpResponse(json.dumps(digest['data'], ensure_ascii=False), content_type="application/json")