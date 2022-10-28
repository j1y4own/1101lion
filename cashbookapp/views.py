from unicodedata import name
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm, CommentForm, HashtagForm
from django.utils import timezone
from .models import Cashbook, Comment,Hashtag
from django.http import request

# Create your views here.
def main(request):
    return render(request, 'main.html')


def write(request):
    if request.method == 'POST':
        form = CashbookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.user = request.user
            form.save()
            return redirect('main')
    else:
        form = CashbookForm
        return render(request, 'write.html', {'form':form})

def read(request):
    cashbooks = Cashbook.objects
    return render(request, 'read.html', {'cashbooks':cashbooks})

def detail(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.cashbook_id = cashbooks
            comment.text = form.cleaned_data['text']
            comment.save()
            id = id
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'cashbooks':cashbooks, 'form':form})

def edit(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CashbookForm(request.POST, request.FILES, instance=cashbooks)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = CashbookForm(instance=cashbooks)
        return render(request,'edit.html', {'form':form})

def delete(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    cashbooks.delete()
    return redirect('read')

def update_comment(request, com_id, id):
    comment = Comment.objects.filter(id=com_id)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance = comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail',id)
    return render(request, 'update_comment.html', {'form':form})

def hashtag(request, hashtag = None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance= hashtag)
        if form.is_valid():
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']) :
                form = HashtagForm()
                error_message = '이미 존재하는 해시태그입니다.'
                return render(request, 'hashtag.html', {'form':form, 'error_message': error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else :
        form = HashtagForm(instance= hashtag)
        return render(request, 'hashtag.html', {"form" : form})


# 좋아요 기능
def likes(request, id):
    like_b = get_object_or_404(Cashbook, id = id)
    if request.user in like_b.post_like.all():
        like_b.post_like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.post_like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('detail', like_b.id)