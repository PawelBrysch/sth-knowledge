from django.http import HttpResponse

# NOTE
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")