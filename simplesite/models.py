# -*- coding:utf8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify


def get_slugified_file_name(filename):
    """
    Takes a filename string and slugify the file name and append its extension.
    This function will return a modified string like the next pattern:
    -- slugified-file-name.FILE_EXTENSION --
    """
    splitted_file_name = filename.split('.')
    slugified_file_name = slugify(splitted_file_name[0]) + '.' + splitted_file_name[1]
    del splitted_file_name
    return slugified_file_name

def get_file_path(instance, filename):
    """
    Builds a path taking an instance and a file name. The object instance is 
    used to get META attributes(for dynamic storage), and the filename is used
    like a arg of other function to normalize names across application.
    """
    return '{0}/{1}/{2}'.format(instance._meta.app_label,
                                str(instance.page.pk),
                                get_slugified_file_name(filename)
                                )


@python_2_unicode_compatible
class Page(models.Model):
    """
    Base object to manage site. 
    """
    title =  models.CharField('Title', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    creation_date = models.DateTimeField('Creation Date', auto_now_add=True) 
    last_modification = models.DateTimeField('Last Modification', auto_now=True) 
    content = models.TextField('Main Content', blank=True, null=True)

    sort_order = models.IntegerField('Sort Order', blank=True, null=True, default=1)
    _related_model = models.ForeignKey(ContentType, verbose_name='Related Content',
                                       related_name='_related_model', blank=True, null=True)
    is_header = models.BooleanField('Belongs to Header', default=False)
    is_footer = models.BooleanField('Belongs to Footer', default=False)

     
    class Meta:
        ordering = ['sort_order', 'slug', 'creation_date']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        return super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('simplesite:page_detail', kwargs={'slug': self.slug})

    @property
    def related_objects(self):
        """
        Returns a QuerySet of related objects gotten by '_related_objects' 
        field.

        object.related_object
        >>> [<Model: object_representation>, <Model: object_representation>]
        """
        try:
            related_qs = self._related_model.get_all_objects_for_this_type()
        except: 
            return None
        return related_qs


@python_2_unicode_compatible
class PageImage(models.Model):
    """
    Image associated to the page 
    """
    title =  models.CharField('Title', max_length=255)
    caption = models.CharField('Caption', max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=get_file_path, max_length=255, blank=True, null=True)
    page = models.ForeignKey(Page, related_name='image_set')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title 
