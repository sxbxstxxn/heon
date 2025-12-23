from django.shortcuts import render

# Create your views here.
def web(request):
	return render(request,'base.html')

def example(request):
	return render(request,'example.html')