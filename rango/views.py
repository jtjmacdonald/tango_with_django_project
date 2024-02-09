from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict['categories'] = category_list
    print(page_list)
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by James"}

    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        
        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    #http post
    if request.method == 'POST':
        form = CategoryForm(request.POST)

    if form.is_valid():
        form.save(commit=True)

        return redirect('rango/')
    else:
        #errors
        print(form.errors)

# Create your views here. (whoops!)

