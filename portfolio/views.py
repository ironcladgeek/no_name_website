from django.shortcuts import render

# Create your views here.
def index(request):
    context={"experience":"","skills":"","languages":"","summary":"","contact":""}
    return render(request, 'portfolio/base.html',context)