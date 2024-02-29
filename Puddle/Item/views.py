from urllib import request
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, Category
from .forms import NewItemForm, EditItemForm, NewCategoryForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)

    return render(request, 'Item/detail.html', {'item':item, 'related_item':related_item})

def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    if query:
        items = items.filter(Q(name__icontains=query)|Q(description__icontains=query))
    if category_id:
        items = items.filter(category_id=category_id)
    context = {
        'items':items,
        'title': 'Items',
        'categories':categories,
        'category_id': int(category_id),
        'query': query
    }
    return render(request, 'Item/items.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        item = validateform(form, request)
        return redirect('Item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {'form':form})

def newcategory(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST)
        item = validateform(form, request)
        return redirect('Item:newitem')
    else:
        form = NewCategoryForm()
    return render(request, 'Item/newcat.html', {'form': form})

def validateform(form, request):
    form = form
    if form.is_valid():
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()
        return item
    



@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('Dashboard:dashboard')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()
            return redirect('Item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/editform.html', {'form':form, 'title':'Edit Item'})
