# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView
from .models import Podcast


class PodcastIndexView(ListView):
    model = Podcast
    paginate_by = 8
    queryset = Podcast.objects.order_by('-pub_date')
    template_name = "podcast/podcast_list.html"

def detail(request, podcast_id):
    current_podcast = Podcast.objects.get(id=podcast_id)
    current_podcast.addView()
    template = loader.get_template('podcast/podcast_detail.html')
    context = RequestContext(request, {'podcast': current_podcast})
    return HttpResponse(template.render(context))
