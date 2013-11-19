from django.http import HttpResponse, Http404
from django.db.models import Q
from django.shortcuts import render
from django.template.loader import render_to_string
from core.models import Page
from rca.models import EventItemDatesTimes, EventItem
from constants import SCREEN_CHOICES, SCREEN_CHOICES_DICT
from rca_signage.templatetags import rca_signage_tags
import datetime
import json


class ScreenIndex(Page):
    indexed = False

    def route(self, request, path_components):
        # If this page is not published, raise 404 error
        if not self.live:
            raise Http404

        if path_components:
            # Request is for a screen
            return self.serve(request, screen=path_components[0], extra_path='/'.join(path_components[1:]))
        else:
            # Request is for screens index
            return self.serve(request)

    def get_upcoming_events(self, start_date=None, max_days=7, max_events=10):
        # Get start date
        if start_date is None:
            start_date = datetime.date.today()
        events = []

        for day_num in range(max_days):
            # Work out date
            date = start_date + datetime.timedelta(days=day_num)

            # Get event dates times for this day
            event_dates_times = EventItemDatesTimes.objects.filter(page__live=True).filter(
                Q(date_from__lte=date, date_to__gte=date) | # Multi day events
                Q(date_from=date, date_to=None) # Single day events
            )

            # Add all events for this day to events list
            for event_date_time in event_dates_times:
                events.append((date, event_date_time))
                if len(events) >= max_events:
                    return events

        return events

    def serve_data(self, request, screen):
       # Check for special event
        special_events = EventItemDatesTimes.objects.filter(page__screens__screen=screen, page__special_event=True, page__live=True)
        if len(special_events) > 0:
            # Special event found, get special events
            new_special_events = [{
                    'date': rca_signage_tags.date_display(datetime.date.today()),
                    'times': rca_signage_tags.event_times_display(event),
                    'title': event.page.title,
                    'location': rca_signage_tags.event_location_display(event),
                    'specific_directions': event.page.specific_directions,
                }
                for event in special_events
            ]
            data = dict(is_special=True, events=new_special_events)
        else:
            # No special events, get upcoming events instead
            upcoming_events = [{
                    'date': rca_signage_tags.date_display(event[0]),
                    'times': rca_signage_tags.event_times_display(event[1]),
                    'title': event[1].page.title,
                    'location': rca_signage_tags.event_location_display(event[1]),
                }
                for event in self.get_upcoming_events()
            ]
            data = dict(is_special=False, events=upcoming_events)

        # Return as JSON
        return HttpResponse(json.dumps(data))

    def serve_screen(self, request, screen, extra_path=None):
        if extra_path == '':
            return render(request, 'rca_signage/screen.html', {
                    'screen': dict(slug=screen, name=SCREEN_CHOICES_DICT[screen]),
                })
        elif extra_path == 'data':
            return self.serve_data(request, screen)
        else:
            raise Http404

    def serve(self, request, screen=None, extra_path=None):
        # Check if this request is for a screen
        if screen:
            # Check that screen exists
            if not screen in SCREEN_CHOICES_DICT:
                raise Http404("Screen doesn't exist")

            return self.serve_screen(request, screen, extra_path=extra_path)
        else:
            return render(request, 'rca_signage/index.html', {
                'screens': [dict(slug=screen[0], name=screen[1]) for screen in SCREEN_CHOICES],
            })