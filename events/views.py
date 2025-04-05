from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    
def event_detail(request: HttpRequest, event_id: int) -> HttpResponse:
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})

@login_required
def edit_event(request: HttpRequest, event_id: int) -> HttpResponse:
    event = get_object_or_404(Events, pk=event_id)

    # Check if the current user is the owner of the event
    if event.user != request.user:
        messages.error(request, "You are not authorized to edit this event.")
        return redirect('events:detail', event_id=event.id)  # Redirect to event detail

    if request.method == 'POST':
        form = AddEventForm(request.POST, instance=event)  # Pass instance to update existing event
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect('events:detail', event_id=event.id)
    else:
        form = AddEventForm(instance=event)  # Populate form with existing event data

    return render(request, 'events/edit_event.html', {'form': form, 'event': event})
