from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from events.forms import AddEventForm

from .models import Events


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "events/index.html")

@login_required
def event_list(request: HttpRequest) -> HttpResponse:
    events = Events.objects.filter(user=request.user)
    if request.headers.get("HX-Request"):
        return render(request, "events/partials/list.html", {"events": events})
    return render(request, "events/list.html", {"events": events})

@login_required
def add_event(request: HttpRequest ) -> HttpResponse:
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect("events:list")
    else: 
        form = AddEventForm()
    return render(request, "events/add_event.html", {"form": form})
    
