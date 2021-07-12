from typing import FrozenSet
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, VisitForm

def main(request):
    return render(request, 'sioreum/main.html', {})

def poetList(request):
    poets = Post.objects.all()
    return render(request, 'sioreum/poetList.html', {'poets':poets})

def poetDetail(request,pk):
    poet = get_object_or_404(Post, pk=pk)
    return render(request, 'sioreum/poetDetail.html', {'poet': poet})

def visitList(request):
    visits = VisitForm.objects.all().order_by('created_date')
    return render(request, 'sioreum/visitList.html', {'visits':visits})