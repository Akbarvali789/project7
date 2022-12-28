from django.shortcuts import render

# Create your views here.
def project7(request):
    d={'name':'Akbar' }
    return render(request,'template.html',d)
