
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from Item.models import Item, Category
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    category = Category.objects.all()

    return render(request, 'core/index.html',{'items':items, 'category':category} )

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_item = Item.objects.filter(category_id=pk)
    return render(request, 'core/category.html', {'category':category, 'category_item':category_item})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:

        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form':form,
        'title':'New Item'})


def signout(request):
    logout(request)
    return redirect('/')