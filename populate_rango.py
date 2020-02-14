import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django 
django.setup() 
from rango.models import Category, Page 

def populate(): 
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.


    python_pages = [
        {'title': 'Official Python Tutorial', 'url':'http://docs.python.org/3/tutorial/', 'views':20}, 
        {'title':'How to Think like a Computer Scientist', 'url':'http://www.greenteapress.com/thinkpython/', 'views':25},
        {'title':'Learn Python in 10 Minutes', 'url':'http://www.korokithakis.net/tutorials/python/', 'views':30} ] 

    django_pages = [
        {'title':'Official Django Tutorial', 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 10},
        {'title':'Django Rocks', 'url':'http://www.djangorocks.com/', 'views': 18}, 
        {'title':'How to Tango with Django', 'url':'http://www.tangowithdjango.com/', 'views': 5}, ] 

    other_pages = [ 
        {'title':'Bottle', 'url':'http://bottlepy.org/docs/dev/', 'views':14}, 
        {'title':'Flask', 'url':'http://flask.pocoo.org', 'views':12} ] 

    nested = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages}, 
            'Other Frameworks': {'pages': other_pages} }

    cats = [{'name': 'Python', 'views': 128, 'likes':64},
            {'name': 'Django', 'views': 64, 'likes': 32},
            {'name': 'Other Frameworks', 'views': 32, 'likes': 16}]

    for cat in cats: 
        add_cat(cat['name'], cat['views'], cat['likes'])


    for cat, cat_pair in nested.items():
        c = Category.objects.filter(name = cat) [0]

        for page in cat_pair['pages']:
            add_page(c, page['title'], page['url'], page['views'])


    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
             print(f'- {c}: {p}') 





def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save() 
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views= views, likes=likes)[0]  
    c.save() 
    return c





# execution starts here
if __name__ == '__main__':
    print('Starting Rango population script...') 
    populate()











