from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

from cercleforme.models import CourseType, Room, Course


def home(request):
    return render(request, "home.html", {
        "types": CourseType.objects.all(),
        "rooms": Room.objects.all()
    })


@require_POST
def search_course(request):
    day_id = request.POST.getlist("day[]", request.POST.get("day", None))
    type_id = request.POST.getlist("type[]", request.POST.get("type", None))
    room_id = request.POST.getlist("room[]", request.POST.get("room", None))
    time = request.POST.getlist("time[]", request.POST.get("time", None))

    courses = Course.objects.all()

    if type_id:
        courses = courses.filter(type_id__in=CourseType.objects.filter(id__in=type_id).values_list("id", flat=True))

    if room_id:
        courses = courses.filter(room_id__in=Room.objects.filter(id__in=room_id).values_list("id", flat=True))

    if day_id:
        # TODO: Mumu ?
        pass

    if time:
        # TODO: Mumu ?
        pass

    return JsonResponse(
        {"courses": [
            {
                "id": course.id,
                "name": course.name,
                "start_time": course.start_time,
                "end_time": course.end_time
            }
            for course in courses]
        }
    )
