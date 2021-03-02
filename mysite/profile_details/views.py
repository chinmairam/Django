from django.shortcuts import render
from django.http import HttpResponse
from .forms import User_Profile_Form
from .models import User_Profile

# Create your views here.


def index(request):
    return HttpResponse("Hello, You are at Profile Index")


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_profile(request):
    if request.method == 'POST':
        form = User_Profile_Form(request.POST)
        if form.is_valid():
            # user_pr = form.save(commit=False)
            # user_pr.display_picture = request.FILES['display_picture']
            # file_type = user_pr.display_picture.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     return render(request, 'error.html')
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            #form = User_Profile.objects.all()[1]
            form.save()
            #user_pr.save()
            return HttpResponse("Details Inserted" + fname)
            #return render(request, 'details.html', {'form': form})
        else:
            form = User_Profile_Form(request.POST)
            return render(request, 'create.html', {'form': form})
    else:
        form = User_Profile_Form()
        return render(request, 'create.html', {'form': form})
