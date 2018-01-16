from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
from django.http import Http404
# from django.template import loader [first way to render template]

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    '''
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) +'/'
        html += '<a href="'+ url +'">'+ album.album_title +'</a><br>'
    '''
    # template = loader.get_template('music/index.html') [first way to render template]    
    # return HttpResponse(template.render(context, request)) [first way]
    
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
        print("1")
    except Album.DoesNotExist: 
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album' : album})
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")