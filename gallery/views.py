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
    title = 'New Photos'
    return render(request, 'all-gallery/new.html', {"date": date, "gallery": gallery,"tags":tags })

def single_photo(request,gallery_id):
    try:
        gallery = Gallery.objects.get(pk=gallery_id)
        tags = Tags.display_tags()
    except Post.DoesNotExist:
        raise Http404("The Post does not exist")

    return render(request,'all-gallery/single_photo.html',{"gallery":gallery, "tags":tags})


# tags
def tags(request,tag_id):
    try:
        tags = Tags.objects.get(id = tag_id)
        gallery = Gallery.objects.filter(tags=tags).all()
    except DoesNotExist:
        raise Http404()
    title = 'Tags'
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
        title = 'Search Results'
        return render(request, 'all-gallery/search.html',{"message":message})

def collections(request):
    collected_tags = Tags.display_tags()
    title = 'Collections'
    return render(request,'all-gallery/collections.html', {"tags":collected_tags})
