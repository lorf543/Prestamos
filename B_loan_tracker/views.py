from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'loan_tracker/home.html')