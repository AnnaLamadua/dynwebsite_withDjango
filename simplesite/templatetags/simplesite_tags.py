# *-* coding=utf-8 *-*
from django import template
from django.conf import settings
from django.utils.html import format_html, strip_tags

from simplesite.commons.tagcommons import get_context_object, build_img_tag
from simplesite.models import Page, SocialNetwork

register = template.Library()

DEFAULT_DESCRIPTON = getattr(settings, 'SIMPLESITE_SEO_DESCRIPTION', '').replace('\n', ' ')
DEFAULT_KEYWORDS = getattr(settings, 'SIMPLESITE_SEO_KEYWORDS', '').replace('\n', ' ')

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

@register.simple_tag(takes_context=True)
def seo_title(context):
    """
    Return the text to be putted on <title></title> tag. This tag will return
    the content of seo_title field. If this field is empty, this tag will 
    return the generic title of the Page.

    EX: {% seo_title %}
    """
    seo_title = ''
    try:
        page = get_context_object(context)
        if page.seo_title:
            seo_title = page.seo_title
        else:
            seo_title = page.title
        return seo_title
    except:
        return None

@register.simple_tag(takes_context=True)
def seo_description(context):
    """
    Return the text to be putted on <meta name="description"> tag. This tag 
    will return the content of seo_description field. If this field is empty,
    this tag will return the generic content of the Page with the HTML tags
    striped. If this value neither exists, returns the 'DEFAULT_DESCRIPTION' 
    value which will be taken from 'SIMPLESITE_DEFAULT_KEYWORDS' var set in
    proyect setting or a empty string.

    EX: {% seo_description %}
    """
    seo_description = ''
    try:
        page = get_context_object(context)
        if page.seo_description:
            seo_description = page.seo_description
        elif page.content:
            seo_description = strip_tags(page.content)[:160]
        else:
            seo_description = DEFAULT_DESCRIPTON
        return seo_description
    except:
        return DEFAULT_DESCRIPTON

@register.simple_tag(takes_context=True)
def seo_keywords(context):
    """
    Return the text to be putted on <meta name="keywords"> tag. This tag 
    will return the content of seo_keyword field. If this value doesn't
    exists, will return the 'DEFAULT_KEYWORDS' value which will be taken
    from 'SIMPLESITE_DEFAULT_KEYWORDS' set in proyect setting or a empty
    string.

    EX: {% seo_keywords %}
    """
    seo_keywords = ''
    try:
        page = get_context_object(context)
        if page.seo_keywords:
            seo_keywords = page.seo_keywords
        else:
            seo_keywords = DEFAULT_KEYWORDS
        return seo_keywords
    except:
        return DEFAULT_KEYWORDS
