from turtle import title
from .models import Post , Query
from django.shortcuts import render
from .filters import AwareFilter
# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        print(name)
        new_post = Query.objects.create(
            name=name,
            email=email,
            phone=phone,
            query = query
        )
    return render(request, 'index.html')

    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        print(name)
        new_post = Post.objects.create(
            name=name,
            email=email,
            phone=phone,
            query = query
        )
        return render(request, 'contact.html')
    return render(request, 'contact.html')
def service(request):
    return render(request, 'services.html')
from django.shortcuts import render
from .models import Post
from .filters import AwareFilter

def aware(request):
    posts = Post.objects.all().order_by('-date_created')

    context = {
        "posts": posts,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        post_picture = request.FILES.get('post_picture')
        new_post = Post.objects.create(
            name=name,
            title=title,
            description=description,
            post_picture=post_picture
        )

    return render(request, 'awareness.html', context)

def post(request):
 
    return render(request,'post.html')
