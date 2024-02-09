import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 100
         },
         {'title': 'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 99
         },
         {'title': 'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 98
         },
        ]
    django_pages = [
         {'title': 'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 97
         },
         {'title': 'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 96
         },
         {'title': 'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 95
         }]
    
    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 94},
         {'title':'Flask',
          'url':'http://flask.pocoo.org',
          'views': 93} 
          ]
    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64 },
            'Django': {'pages': django_pages, 'views': 64, 'likes' : 32},
            'Other Frameworks': {'pages': other_pages, 'views':32, 'likes':16 }}

    def add_cat(name, views=0, likes=0):
        #in the textbook, this is at the end, moved to fix
        c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
        c.save()
        return c
    
    def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
        p.url=url
        p.views=views
        p.save()
        return p
    
    #add more categories or pages above

    #scan cats dictionary, then add each category
    #then add all associated category pages

    for cat, cat_data in cats.items():

        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    
    
    
    
if __name__=='__main__':
    print('Starting rango population script..')
    populate()
    print("completed with no errors")


