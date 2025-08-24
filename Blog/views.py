from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import SignUpForm, TweetForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm

@csrf_exempt
def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
@csrf_exempt
def TweetList(request):
    tweets = Tweet.objects.all().order_by('created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def CreatTweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
        return render(request, 'tweet_form.html', {'form': form})

@login_required
def EditTweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if tweet.user != request.user:
        return redirect('tweet_list')

    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
        return render(request, 'tweet_form.html', {'form': form})

@login_required
def DelTweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if tweet.user != request.user:
        return redirect('tweet_list')

    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


