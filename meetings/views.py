from django.shortcuts import render, get_object_or_404

from meetings.models import Meeting, Room
from django.forms import modelform_factory


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])

form = MeetingForm()


def new(request):
    return render(request, "meetings/new.html", {"form": form})
