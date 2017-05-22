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
    type_id = request.POST.get("type", None)
    room_id = request.POST.get("room", None)
    time = request.POST.get("time", None)

    if type_id is None or room_id is None or time is None:
        return JsonResponse(status=500)

    type = CourseType.objects.get(id=type_id)
    room = Room.objects.get(id=room_id)
    courses = [{"id": course.id, "name": course.name, "start_time": course.start_time, "end_time": course.end_time} for course in Course.objects.filter(start_time__gte=time, room=room, type=type)]
    return JsonResponse({"courses":courses})
