from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from Item.models import Item


@login_required
def index(request):
    item = Item.objects.filter(created_by=request.user)


    return render(request, 'Dashboard/index.html', {
        'item': item
    })

