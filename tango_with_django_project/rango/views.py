from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br/><strong><a href='/rango/about/'>About</a></strong>")
def about(request):
    return HttpResponse("Rango says here is the about page. <br/><strong><a href='/rango/'>Index</a></strong>")