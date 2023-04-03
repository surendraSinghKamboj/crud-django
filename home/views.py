from django.shortcuts import render,HttpResponse
import platform

# Create your views here.
def index(request):
    system = platform.system()
    release = platform.release()
    context = {
        "heading":system +" "+ release
    }
    return render(request,"index.html",context)