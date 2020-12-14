from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Quote
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validation(request.POST)
        if User.objects.filter(email=request.POST['email']):
            messages.error(request, 'email is already used')
            return redirect('/')
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            new_user = User.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=pw_hash)
            request.session['userid'] = new_user.id
            return redirect('/success')
    return redirect('/')


def success(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            context = {
                'user': user[0]
            }
            return render(request, 'success.html', context)
    return redirect('/')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')

    return redirect('/')


def logout(request):
    if request.session['userid']:
        print('logging out')
        request.session['userid'] = None
    return redirect('/')


def quotes(request):
    quote = Quote.objects.all()
    current_user = User.objects.get(id=request.session['userid'])
    context = {
        'quotes': quote,
        'current_user': current_user
    }
    return render(request, 'quotes.html', context)


def write_quote(request):
    if request.method == "POST":
        errors = Quote.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/quotes')
        else:
            Quote.objects.create(
                quote=request.POST['quote'],
                quoted_by=request.POST['quoted_by'],
                quote_owner=User.objects.get(id=request.session['userid'])
            )
            return redirect('/quotes')
    return redirect('/quotes')


def user_profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


def favorite(request, id):
    fav_quote = Quote.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['userid'])
    fav_quote.user_like.add(user_liking)
    return redirect('/quotes')


def unfavorite(request, id):
    fav_quote = Quote.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['userid'])
    fav_quote.user_like.remove(user_liking)
    return redirect('/quotes')


def edit(request, id):
    quote = Quote.objects.get(id=id)
    context = {
        'quote': quote
    }
    return render(request, 'edit.html', context)


def delete(request, id):
    quote = Quote.objects.get(id=id)
    quote.delete()
    return redirect('/quotes')


def edit_quote(request, id):
    if request.method == "POST":
        errors = Quote.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/edit/'+str(id))
        else:
            pointer = Quote.objects.get(id=id)
            pointer.quote = request.POST['quote']
            pointer.quoted_by = request.POST['quoted_by']
            pointer.save()
            return redirect('/quotes')
    return redirect('/quotes')
