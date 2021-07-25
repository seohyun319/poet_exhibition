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
    visits = VisitForm.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    # if page==1:
    #     paginator = Paginator(visits, 3)
    # else: 
    paginator = Paginator(visits, 7)
    try:
        visits = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        visits = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        visits = paginator.page(paginator.num_pages)
    return render(request, 'sioreum/visitList.html', {'visits':visits})

@ method_decorator(csrf_exempt)
def visitCreate(request):
    if request.method == 'GET':
        visits = VisitForm.objects.all().order_by('-created_date')
        return render(request, 'sioreum/visitList.html', {"visits":visits})

    elif request.method == 'POST':
        req = json.loads(request.body)
        # id = req['id']
        content = req['content']
        name = req['name']
        # date = req['date']
        # y=date[2:4]
        # m=date[5:7]
        # d=date[8:10]
        # time=y+'.'+m+'.'+d
        # phone = req['phone']
        if content:
            visitNew = VisitForm(
                text=content, author=name, 
                # created_date=time,
                # phone=phone 
                )
            visitNew.save()
        return JsonResponse({'comment':visitNew.text, 'writer':visitNew.author, 'time':visitNew.created_date, 
        # 'y':y, 'm':m, 'd':d, 
        })

# def visitCreate(request):
#     content = get_param(request, 'content', '')
#     name = get_param(request, 'name', '')


#     return HttpResponse(json.dumps(context), content_type='application/json')


    

# def create(request):
#     if request.method == 'POST':
#         form = VisitForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('sioreum:visitor')
#     else: 
#         form = VisitForm()
#         ctx = {'form':form}
#         return render(request, 'sioreum/visitList.html', ctx)

    
# def update(request, pk):
#     visits = get_object_or_404(visitList, id=pk)
#     if request.method == 'POST':
#         form = VisitForm(request.POST, instance=visits)
#         if form.is_valid():
#             post = form.save()
#             return redirect('sioreum:visitor', pk)
#     else:
#         form = VisitForm(instance=post)
#         ctx = {'form': form}
#         return render(request, 'sioreum/visitList.html', ctx)


# def delete(request, pk):
#     visits = get_object_or_404(visitList, pk=pk)
#     if request.method == 'GET':
#         return redirect('sioreum:visitor', visits.id)
#     elif request.method == 'POST':
#         visits.delete()
#         return redirect('sioreum:visitor')