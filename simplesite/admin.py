# -*- coding:utf8 -*-

from django import forms
from django.contrib import admin

from simplesite.models import Page, PageImage

class PageImageInline(admin.TabularInline):
    """
    Stack inline choice items to be displayed in Page Admin Panel
    """
    model = PageImage 
    extra = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    Customizing Page Model representation in Django Admin
    """
    fieldsets = [
            (None, {
                'fields': [
                    'title',
                    'slug',
                    ('sort_order', '_related_model' ,'is_header', 'is_footer',),
                    'content',
                    ]
                }),
            ]

    prepopulated_fields = {'slug': ('title',)}
    inlines = [PageImageInline]
    list_display = (
            'id',
            'title',
            'slug',
            'sort_order',
            'last_modification',
            )
    list_display_links = ('id', 'title',)
    search_fields = ['title', 'pk']
