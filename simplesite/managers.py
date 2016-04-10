from django.db import models

class PageManager(models.Manager):
    """
    Manager for Page objects.
    """
    def get_public_pages(self, *args, **kwargs):
        """
        Returns public pages.
        """
        return self.get_queryset(*args, **kwargs).filter(is_public=True)
