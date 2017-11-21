from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Gallery

# trending photos
def trending_photos(request,past_date):

    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(new_photos)

    gallery = Gallery.trending_now(date)
    return render(request, 'all-gallery/trending.html', {"date": date,})

# new photos
def new_photos(request):
    date = dt.date.today()


    gallery = Gallery.get_images
    return render(request, 'all-gallery/new.html', {"date": date, "gallery": gallery, })

# search photos
def search_results(request):

    if 'tag' in request.GET and request.GET["tag"]:
        search_term = request.GET.get("tag")
        searched_tags = Tag.search_by_tag(search_term)
        photos = Photo.objects,filter(tags = searched_tags).all()
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"tags": searched_tags, "photos":photos})
    else:
        message = "No photos searched"
        return render(request, 'all-gallery/search.html',{"message":message})
