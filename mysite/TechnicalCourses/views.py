from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Allcourses, details
from django.template import loader
# Create your views here.


def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('Courses.html')
    context = {'ac': ac}
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    course = get_object_or_404(Allcourses, pk=course_id)
    return render(request, 'detail.html', {'course': course})
    # try:
    #     course = Allcourses.objects.get(pk=course_id)
    # except Allcourses.DoesNotExist:
    #     raise Http404("Course Not Available")
    # return render(request, 'detail.html', {'course': course})


def yourchoice(request, course_id):
    course = get_object_or_404(Allcourses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'detail.html', {'course': course, 'error_message': "Select a valid option"})
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'detail.html', {'course': course})
