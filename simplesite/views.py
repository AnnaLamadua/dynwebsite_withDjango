# -*- coding:utf8 -*-
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView

from simplesite.models import Page


class PageBaseDetailView(DetailView):
    """
    Base View model specification. The remain views, will inherit from this 
    across de application.
    """
    model = Page

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Page.objects.all()
        return Page.objects.get_public_pages()

    def get_object(self):
        page_qs = self.get_queryset()
        page_slug = self.kwargs.get('slug', None)
        try:
            page = page_qs.get(slug=page_slug)
        except:
            raise Http404()
        return page


class IndexDetailView(PageBaseDetailView):
    """
    Render the Home Page. the templates must have one of these names. 
    """

    def get_template_names(self):
        return [
                "simplesite/{0}_page.html".format(self.kwargs.get('slug')),
                "simplesite/index.html",
                "simplesite/home.html",
                ] 
        

class PageDetailView(PageBaseDetailView):
    """
    Render the NON home Page objects. This view takes the slug kwargs and
    searchs the template looking for the next pattern.
    """

    def get_template_names(self):
        return [
                "simplesite/{0}_page.html".format(self.kwargs.get('slug')),
                "simplesite/page_detail.html",
                ] 
