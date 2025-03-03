from django.shortcuts import render,redirect
from channel.models import Channel
from core.models import Video
from channel.forms import VideoForm
from channel.forms import ChannelForm
from django.contrib import messages
from userauths.models import Profile

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
    user = Profile.objects.get(user=request.user)
    if channel in user.subscriptions.all():
        videos=Video.objects.filter(user=channel.user, visibility="public").order_by("-date")

        context = {
        "videos":videos,
        "channel":channel,
        }
        return render(request,"channel/channel-videos.html",context)    
    else:
        messages.warning(request,"You need to subscribe to channel to view videos")   
    
        return redirect("channel-prof", channel.id)


def your_videos(request,id):
    channel =  Channel.objects.get(id=id)
    videos=Video.objects.filter(user=channel.user, visibility="public").order_by("-date")

    context = {
        "videos":videos,
        "channel":channel,
    }
    
    return render(request,"your_videos.html",context)


def channel_about(request,id):
    channel =  Channel.objects.get(id=id)

    context = {
        "channel":channel,
    }
    
    return render(request,"channel/about.html",context)


def video_upload(request):
    user = request.user
    channel = Channel.objects.get(user=request.user)
    
    
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)             #accepting user data
        if form.is_valid():
            new_form = form.save(commit=False)                    # we are saving form but not commiting to database
            new_form.user= user                                   # new_form.user is database user matching with user variable(user=request.user)
            new_form.save()
            form.save_m2m()                                   #saving many2many field which is tag field
            messages.success(request,f"Video Uploaded Successfully")
            return redirect("index")
        
    else:
            form = VideoForm()
    context = {
            "form":form,
            "channel":channel,
    } 
    return render(request,"channel/upload.html",context)


def video_edit(request, video_id,channel_id):
    user = request.user
    video = Video.objects.get(id=video_id)
    channel = Channel.objects.get(id=channel_id)
    
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES,instance=video)             #The instance=video is used when you want to edit an existing object rather than creating a new one.
        if form.is_valid():
            new_form = form.save(commit=False)                    # we are saving form but not commiting to database
            new_form.user= user                                   # new_form.user is database user matching with user variable(user=request.user)
            new_form.save()
            form.save_m2m()                                   #saving many2many field which is tag field
            messages.success(request,f"Video Edited successfully")
            return redirect("index")
        
    else:
            form = VideoForm(instance=video)
    context = {
            "form":form,
    } 
    return render(request,"channel/upload.html",context)

def video_delete(request, video_id,channel_id):
    user = request.user
    video = Video.objects.get(id=video_id)
    channel = Channel.objects.get(id=channel_id)

    video.delete()
    messages.success(request, "Video deleted successfully.")
    return redirect("index")

def channel_create(request):
    user = request.user
    
    if request.method == "POST":
        form = ChannelForm(request.POST, request.FILES)             #accepting user data
        if form.is_valid():
            new_form = form.save(commit=False)                    # we are saving form but not commiting to database
            new_form.user= user                                   # new_form.user is database user matching with user variable(user=request.user)
            new_form.save()
            form.save_m2m()                                   #saving many2many field which is tag field
            messages.success(request,f"Channel Created Successfully")
            return redirect("index")
        
    else:
            form = ChannelForm()
    context = {
            "form":form,
    } 
    
    return render(request,"channel/create_channel.html",context)


def channel_edit(request):
    user = request.user
    channel = Channel.objects.get(user=request.user)
    
    if request.method == "POST":
        form = ChannelForm(request.POST, request.FILES,instance=channel)             #accepting user data
        if form.is_valid():
            new_form = form.save(commit=False)                    # we are saving form but not commiting to database
            new_form.user= user                                   # new_form.user is database user matching with user variable(user=request.user)
            new_form.save()
            form.save_m2m()                                   #saving many2many field which is tag field
            messages.success(request,f"Channel Edited Successfully")
            return redirect("index")
        
    else:
            form = ChannelForm(instance=channel)
    context = {
            "form":form,
            "channel":channel,
    } 
    
    return render(request,"channel/create_channel.html",context)


def channel_delete(request,id):
    channel = Channel.objects.get(id=id)
    channel.delete()
    return redirect("index")
    
    
    
    