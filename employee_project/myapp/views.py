from django.shortcuts import render

# Create your views here.
def myapp(request):
    foorm='2'
    if request.method == "POST":
        foorm= request.POST
       

    return render(request, 'myapp/index.html', {'foorm' : foorm})