from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, "posts/post_list.html")

def post_add(request):
    return render(request, "posts/post_add.html")