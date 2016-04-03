# -*- coding:utf8 -*-

from django.shortcuts import render
from django.views.generic import DetailView

from simplesite.models import Page


class PageBaseDetailView(DetailView):
    """
    Base View model specification. The remain views, will inherit from this 
    across de application.
    """
    model = Page

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
