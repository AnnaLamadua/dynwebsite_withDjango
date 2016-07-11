# *-* coding=utf-8 *-*

"""
A collection of functions to serve and keep template tags file clean.

"""

from django.utils.html import mark_safe

def get_context_object(context):
    """
    Try to return the object instance in the context. On Except, bubble the 
    exeption to the call.
    """
    try:
        obj = context['object']
        return obj
    except Exception:
        raise

def build_img_tag(img):
    """
    Build a HTML Img TAG with the given img object.
    """
    img_tag = '<img src="{0}" alt="{1}" />'.format(img.image.url, img.title)
    return mark_safe(img_tag)
