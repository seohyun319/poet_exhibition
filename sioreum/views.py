from typing import FrozenSet
from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, VisitForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

def main(request):
    return render(request, 'sioreum/main.html', {})

def poetList(request):
    poets = Post.objects.all()
    return render(request, 'sioreum/poetList.html', {'poets':poets})

def poetDetail(request,pk):
    poet = get_object_or_404(Post, pk=pk)
    return render(request, 'sioreum/poetDetail.html', {'poet': poet})

def visitList(request):
    visit_all = VisitForm.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    if (page=="1"):
        paginator = Paginator(visit_all, 5)    
    else : paginator = Paginator(visit_all, 6)
    try:
        visits = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        visits = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        visits = paginator.page(paginator.num_pages)
    # Get the index of the current page
    index = visits.number - 1  
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    ctx = {'visit_all':visit_all, 'visits':visits, 'page_range': page_range}
    return render(request, 'sioreum/visitList.html', ctx)

@ method_decorator(csrf_exempt)
def visitCreate(request):
    if request.method == 'GET':
        visits = VisitForm.objects.all().order_by('-created_date')
        return render(request, 'sioreum/visitList.html', {"visits":visits})
    elif request.method == 'POST':
        req = json.loads(request.body)
        content = req['content']
        name = req['name']
        number = req['number']
        if content:
            visitNew = VisitForm(
                text=content, author=name, phone=number,
                )
            visitNew.save()
        return JsonResponse({'comment':visitNew.text, 'writer':visitNew.author, 'time':visitNew.created_date })
