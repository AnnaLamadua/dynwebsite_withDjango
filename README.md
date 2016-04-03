# Simple Site

*Django app to create and manage simple websites with a basic Page model which can create generic relations with any other model to get its full queryset*


### Features

**TO DOC**


### Requirements

Simple Site is developed and require Django>=1.9, pillow and Python > 2.7

### How to install it

It can be installed via pip running the next command.
```
pip install git+http://github.com/mars0n/simple-site.git
```

After installation, you must include it in your ```settings.py```. You can add it via the app config file, or the appname
```
INSTALLED_APPS = [
    ...
    # Via config file
    'simplesite.apps.SimplesiteConfig',
    ...
    # Via appname
    'simplesite',
]
```
Then add it in ```urls.py```:
```
urlpatterns = [
    ...
    url(r'', include('simplesite.urls')),
    ]
```
Finally, run the migration executing ```python manage.py migrate```

**Congrats, it's ready!***

### Default URLs and Views

The the slug of Index Page *must be named* **'home'** to use the built-in `index_page` view. The other pages, can have any name and will be use the `page_detail` view.

|     View name   |URL              |
|-----------------|-----------------|
|`index_page`     |`/`              |
|`page_detail`    |`/<slug>/`       |

### Templates

It's recommended to name the templates like next patterns, the views will look for the templates through the following pattern:

**INDEX PAGE:**
```
"simplesite/<page_slug>_page.html",
"simplesite/index.html",
"simplesite/home.html",
```
**PAGE DETAIL:**
```
"simplesite/<page_slug>_page.html",
"simplesite/page_detail.html",
```

The template ```simplesite/page_detail.html"``` is used like **generic template**. If a page haven't a template named like the pattern, the view looks for the generic one.

### Template Tags

#### {% get_header_list %}
*Assignment tag*
Returns a QuerySet of Page objects  that belong to header

Ex:
``` {% get_header_list as header_object_list %} ```

#### {% get_footer_list %}
*Assignment tag*
Returns a QuerySet of Page objects  that belong to footer

Ex:
``` {% get_footer_list as footer_object_list %} ```

### Author
[https://github.com/mars0n/](https://github.com/mars0n/)
