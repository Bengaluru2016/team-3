from django.shortcuts import render

def index_page(request):
    return render(request, 'samridhi_site/index.html', {})
# Create your views here.
