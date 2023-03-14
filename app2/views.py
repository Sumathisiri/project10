from django.shortcuts import render

# Create your views here.
def project10(request):
    d={'name':'sireesha','Age':22,'graduation':'BSC(biotech)'}
    return render(request,'jinja_print.html',context=d)


def project(request):
    d={'name':'sumathi','Age':23}
    return render(request,'jinja_print.html',context=d)


