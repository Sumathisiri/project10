from django.shortcuts import render

# Create your views here.


def jinja_print(request):
    d={'name':'suresh'}
    return render(request,'jinja_print.html',context=d)


def second(request):
    d={'name':'saiii','Age':25}
    return render(request,'jinja_print.html',context=d)
