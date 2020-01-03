from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Movie
# Create your views here.
'''
def home(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'core\index.html',context) 
'''

class MovieList(ListView):
    model = Movie
    
class MovieDetail(DetailView):
    model = Movie