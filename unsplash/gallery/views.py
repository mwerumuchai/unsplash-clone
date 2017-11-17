from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt


def welcome(request):
    return render(request, 'welcome.html')

def new_photos(request):
    date = dt.date.today()

    return render(request, 'all-gallery/new.html', {"date": date,})

# trending photos
def trending_photos(request,past_date):

    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(new_photos)

    return render(request, 'all-gallery/trending.html', {"date": date})
