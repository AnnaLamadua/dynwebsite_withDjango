# *-* coding=utf-8 *-*
from django import template
from django.utils.html import format_html

from simplesite.commons.tagcommons import get_context_object, build_img_tag
from simplesite.models import Page, SocialNetwork


register = template.Library()

@register.simple_tag
def get_header_list():
    """
    Returns a list of public pages that belong to header
    """
    return Page.objects.get_public_pages().filter(is_header=True)

@register.simple_tag
def get_footer_list():
    """
    Returns a list of public pages that belong to header
    """
    return Page.objects.get_public_pages().filter(is_footer=True)

@register.simple_tag
def get_page(**kwargs):
    """
    Returns a public page object filtered by the given kwargs
    """
    try:
        page = Page.objects.get_public_pages().get(**kwargs)
    except:
        page = None
    return page

@register.simple_tag
def get_all_social_networks():
    """
    Returns all SocialNetwork objects
    """
    return SocialNetwork.objects.all()

@register.simple_tag
def get_active_social_networks():
    """
    Returns active SocialNetwork objects
    """
    return SocialNetwork.objects.filter(is_active=True)

@register.simple_tag(takes_context=True)
def detail_image(context):
    """
    Render the first detail image of the Page
    """
    try:
        obj = get_context_object(context)
        img = obj.image_set.filter(img_type='detail').first()
        img_tag = build_img_tag(img)
        return img_tag
    except:
        return

@register.simple_tag(takes_context=True)
def thumbnail_image(context):
    """
    Render the first thumbnail image of the Page
    """
    try:
        obj = get_context_object(context)
        img = obj.image_set.filter(img_type='thumbnail').first()
        img_tag = build_img_tag(img)
        return img_tag
    except:
        return

@register.simple_tag(takes_context=True)
def get_gallery_images(context):
    """
    Returns a list of img related objects selected as 'gallery'
    """
    try:
        obj = get_context_object(context)
        return obj.image_set.filter(img_type='gallery')
    except:
        return []

@register.simple_tag(takes_context=True)
def page_content(context):
    """
    Check if the given instance wrapped in the context is a Page one. Then 
    parse the content of te page to HTML.
    EX: {% page_content %}
    """
    try:
        page = get_context_object(context)
        if isinstance(page, Page):
            return format_html(page.content)
    except: 
        return ''