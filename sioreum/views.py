from typing import FrozenSet
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, VisitForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main(request):
    return render(request, 'sioreum/main.html', {})

def poetList(request):
    poets = Post.objects.all()
    return render(request, 'sioreum/poetList.html', {'poets':poets})

def poetDetail(request,pk):
    poet = get_object_or_404(Post, pk=pk)
    return render(request, 'sioreum/poetDetail.html', {'poet': poet})

def visitList(request):
    visits = VisitForm.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(visits, 8)
    try:
        visits = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        visits = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        visits = paginator.page(paginator.num_pages)
    return render(request, 'sioreum/visitList.html', {'visits':visits})

def create(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('sioreum:visitor')
    else: 
        form = VisitForm()
        ctx = {'form':form}
        return render(request, 'sioreum/visitList.html', ctx)