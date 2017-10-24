# Simple Site
 ***SimpleSite*** *is a single Django app to create and manage dynamic websites. It's based on a base model* ***Page***  *which will be created to get a easy customization of your Site. The unique purpose of this app is to be connected with other models. Creating and connecting your custom models with Page instances, you ensure a full customization of your project and keeping the clean URLs this app brings to you.*

## Features

* Create any pages you want and connect each one with any other model via ContentType generic relationships.
* Manage page status (Public & Draft) .
* Set page images to be used like Thumbnail, Detail or Cover. 
* Create and manage the link and the status of your social networks.
* Manage the SEO basics of your website.

## Requirements

Simple Site is developed and require Django>=1.9, pillow, Python > 2.7 and django-summernote.

## How to install it

It can be installed via pip running the next command.
```
pip install git+http://github.com/marcopuccio/simple-site.git
```

After installation, you must include it in your ```settings.py```. You can add it via the app config file, or the appname. In adition, you must include the WYSIWYG editor [Django Summernote](https://github.com/summernote/django-summernote) dependency.

```
INSTALLED_APPS = [
    # WYSIWYG editor dependency
    'django_summernote',

    ...
    # SS config file
    'simplesite.apps.SimplesiteConfig',
    ...
    # SS appname
    'simplesite',
]
```
Then add it in ```urls.py```:
```
urlpatterns = [
    ...
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'', include('simplesite.urls')),
    ]
```
Finally, run the migration executing ```python manage.py migrate```

**Congrats, it's ready!***

## Default URLs and Views

The the slug of Index Page *must be named* **'home'** to use the built-in `index_page` view. The other pages, can have any name and will be use the `page_detail` view.

|     View name   |URL              |
|-----------------|-----------------|
|`home_page`      |`/`              |
|`page_detail`    |`/<slug>/`       |

## Templates

It's recommended to name the templates like next patterns, the views will look for the templates through the following pattern:

**INDEX PAGE:**
```
"simplesite/page_<page_slug>.html",
"simplesite/<page_slug>_page.html",
"simplesite/index.html",
"simplesite/home.html",
```

**PAGE DETAIL:**
```
"simplesite/page_<page_slug>.html",
"simplesite/<page_slug>_page.html",
"simplesite/page_detail.html",
```

The template ```simplesite/page_detail.html"``` is used like **generic template**. If a page haven't a template named like the pattern, the view looks for the generic one.

## Template Tags

#### {% get_page %}

Returns a public page object filtered by the given kwargs.

Ex: ```{% get_page [ slug='example' | sort_order=2 ] as ex_page %}```


#### {% page_content %}
Check if the given instance wrapped in the context is a Page one. Then parse the content of te page to HTML.

Ex: ```{% page_content %}```

Returns the same output than```{{ page.content|safe }}```


#### {% detail_image %}
Render the first DETAIL image of the Page. This is a Django ```simple_tag``` that builds a HTML image tag with the given image related to the Page and its title.  

Ex:```{% detail_image %}```

Returns ``` <img src="{{ IMG_PATH }}" alt="{{ IMG_TITLE }}"/>``` 


#### {% thumbnail_image %}
Render the first THUMBNAIL image of the Page. This is a Django ```simple_tag``` that builds a HTML image tag with the given image related to the Page and its title.  

Ex:```{% thumbnail_image %}```

Returns ``` <img src="{{ IMG_PATH }}" alt="{{ IMG_TITLE }}"/>``` 


#### {% get_gallery_images %}
Returns a list of img related objects selected as 'gallery'

Ex:
``` 
{% get_gallery_images as gallery_imgs %}
{% for img in gallery_img %}
<img src="{{ img.image.url }}" alt="{{ img.title }}"/>
{% endfor %}
``` 


#### {% seo_title %}
Return the text to be rendered on ```<title></title>``` tag. This tag will return the content of ```page.seo_title``` field. If this field is empty, this tag will return the generic title of the Page.

Ex: ```{% seo_title %}```


#### {% seo_description %}
Return the text to be rendered on ```<meta name="description">``` tag. This tag will return the content of ```page.seo_description``` field. If this field is empty, this tag will return the generic content of the Page with the HTML tags striped. If this value neither exists, returns the value of ```SIMPLESITE_DEFAULT_KEYWORDS``` var set in proyect settings or a empty string.

Ex: ```{% seo_description %}```


#### {% seo_keywords %}
Return the text to be rendered on ```<meta name="keywords">``` tag. This tag will return the content of ```page.seo_keyword``` field. If this value doesn't exists, will return the value of ```SIMPLESITE_DEFAULT_KEYWORDS``` set in proyect settings or a empty string.

Ex:```{% seo_keywords %}```


### Social Media Template tags 

#### {% get_all_social_networks %}

Returns all SocialNetwork objects.

Ex:```{% get_all_social_networks as socials_object_list %}```


#### {% get_active_social_networks %}

Returns active SocialNetwork objects.

Ex:```{% get_active_social_networks as socials_object_list %}```


### Author
[Marco Puccio](http://marsxn.io/)
