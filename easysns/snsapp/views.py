from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import SnsModel

def signup(request):
  if request.method == "POST":
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # DB内のユーザー一覧に入力されたユーザー名が含まれているか確認
    try:
      # 合致するユーザーがなければDoesNotExistになる
      # except文に移行して、新規に登録が実行される
      User.objects.get(username=username)
      return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
    except:
      User.objects.create_user(username, email, password)
  return render(request, 'signup.html', {'number': 100})

def signin(request):
  if request.method == 'POST':
    # usernameを指定します。
    # emailを使用したい場合は、Userモデルをカスタマイズする必要があります
    username = request.POST['username']
    password = request.POST['password']
    # DBに存在するか確認
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      # renderでも可
      return redirect('page')
    else:
      # 認証失敗時
      return redirect('signin')

  return render(request, 'signin.html')

@login_required
def pagefunc(request):
  object_list = SnsModel.objects.all()
  return render(request, 'page.html', {'object_list':object_list})


def logoutfunc(request):
  logout(request)
  return redirect('signin')

def detailfunc(request, pk):
  object = SnsModel.objects.get(pk=pk)
  return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
  post = SnsModel.objects.get(pk=pk)
  post.good = post.good + 1
  post.save()
  return redirect('page') 

def readfunc(request, pk):
  post = SnsModel.objects.get(pk=pk)
  # ログインユーザーのユーザー名をとる
  post2  = request.user.get_username()
  if post2 in post.readtext:
    return redirect('page')
  else:
    post.read += 1
    post.readtext = post.readtext + " " + post2
    post.save()
    return redirect('page')
