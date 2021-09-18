from django.shortcuts import render

# Create your views here.

def index(request):
	"""The home page for learning logs"""
	return render(request, 'learning_logs/index.html')