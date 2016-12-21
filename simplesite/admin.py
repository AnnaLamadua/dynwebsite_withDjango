# -*- coding:utf8 -*-

from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin

from simplesite.models import (
    Page, PageImage, SocialNetwork
)


class PageImageInline(admin.TabularInline):
    """
    Stack inline choice items to be displayed in Page Admin Panel
    """
    model = PageImage
    extra = 1


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    """
    Customizing Page Model representation in Django Admin
    """
    fieldsets = [
        ('SEO', {
            'fields': [
                'seo_title',
                'seo_description',
                'seo_keywords',
            ],
            'classes': [
                'collapse',
            ]
        }),
        (None, {
            'fields': [
                'title',
                'slug',
                'alternative_url',
                ('sort_order', 'is_public'),
                '_related_model',
                'content',
            ]
        })
    ]

    prepopulated_fields = {'slug': ('title',)}
    inlines = [PageImageInline]
    list_display = (
        'id',
        'title',
        'slug',
        'is_public',
        'sort_order',
        'last_modification',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('is_public', 'creation_date', 'last_modification',)
    search_fields = ['title', 'pk']


@admin.register(SocialNetwork)
class SocialNetworkAdmin(SummernoteModelAdmin):
    """
    Customizing SocialNetwork representation in Django Admin
    """
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                'url',
                ('sort_order', 'is_active'),
                'image',
            ]
        }),
    ]

    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'id',
        'title',
        'slug',
        'is_active',
        'sort_order',
    )
    list_display_links = ('id', 'title',)
    list_display_filter = ('is_active',)
    search_fields = ['title', 'pk']
