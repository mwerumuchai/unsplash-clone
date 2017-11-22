from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Gallery,Tags

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
    tags = Tags.display_tags()
    return render(request, 'all-gallery/new.html', {"date": date, "gallery": gallery,"tags":tags })

# tags
def tags(request,tag_id):
    try:
        tags = Tags.objects.get(id = tag_id)
        gallery = Gallery.objects.filter(tags=tags).all()
    except DoesNotExist:
        raise Http404()
    return render(request,'all-gallery/tag.html', {"tags": tags, "gallery":gallery})

# search photos
def search_results(request):

    if 'tag' in request.GET and request.GET["tag"]:
        search_term = request.GET.get("tag")
        searched_tags = Tags.search_for_tag(search_term)
        gallery = Gallery.objects.filter(tags = searched_tags).all()
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"searched_tags": searched_tags, "gallery":gallery})
    else:
        message = "No photos searched"
        return render(request, 'all-gallery/search.html',{"message":message})
