from django.shortcuts import render

posts = [
    {
        'author': 'Person1',
        'title': 'First post',
        'content': 'Content',
        'date_posted': 'Day Month, Year'
    },
    {
        'author': 'Person2',
        'title': 'First post',
        'content': 'Content',
        'date_posted': 'Day Month, Year'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
