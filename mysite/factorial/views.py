from django.shortcuts import render
from django.http import HttpResponse
from .forms import FactorialForm
from .models import FactorialPost
# Create your views here.


def index(request):
    return render(request, 'input.html')
    # return HttpResponse("<h2>Hello,world. You're at the factorial index.</h2>")


def factorial(request):
    if request.method == 'POST':
        form = FactorialForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num']
            form.save()
            if num.isdigit():
                x = int(num)
                factor = 1
                if x < 0:
                    res = "Factorial does not exist"
                    return render(request, 'result.html', {"result": res})
                elif x == 1:
                    res = x
                    return render(request, 'result.html', {"result": res})
                else:
                    for i in range(1, x+1):
                        factor = factor * i
                        return render(request, 'result.html', {"result": factor})
