from django.shortcuts import render, get_object_or_404

from .models import Item

def allitems(request):
    items= Item.objects
    return render(request, 'item/allitems.html', {'items': items})

def detail(request, item_id):
    detailitem=get_object_or_404(Item, pk=item_id)
    return render(request, 'item/detail.html', {'item': detailitem})
