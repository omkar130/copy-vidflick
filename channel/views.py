from django.shortcuts import render
from channel.models import Channel
from core.models import Video

def channel_profile(request,id):
    channel =  Channel.objects.get(id=id)
    
    videos=Video.objects.filter(user=channel.user, visibility="public").order_by("-views")
    
    video_featured = Video.objects.get(user=channel.user.id) 
    
    context = {
        "channel":channel,                                       #this is actually passing the object to that html page so that page can use it.
        "video_featured":video_featured,
        "videos":videos,
    }
    
    return render(request,"channel/channel.html",context)


def channel_videos(request,id):
    channel =  Channel.objects.get(id=id)
    videos=Video.objects.filter(user=channel.user, visibility="public").order_by("-date")

    context = {
        "videos":videos,
        "channel":channel,
    }
    
    return render(request,"channel/channel-videos.html",context)


def channel_about(request,id):
    channel =  Channel.objects.get(id=id)

    context = {
        "channel":channel,
    }
    
    return render(request,"channel/about.html",context)
