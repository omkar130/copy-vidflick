from django.shortcuts import render
from core.models import Video, Comment
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from channel.models import Channel
from userauths.models import Profile
from django.db.models import Q                      #Q objects are used for complex queries involving AND, OR, and NOT conditions

def index(request):
    video = Video.objects.filter(visibility="public")  # all() ->all video will come. filter()-> particular filter videos will come.
    context = {
        "video": video
    }
    return render(request,'index.html',context)

def videoDetail(request,pk):
    video = Video.objects.get(id=pk)
    channel = Channel.objects.get(user=video.user)
    
    video.views =  video.views + 1
    video.save()              
    
    comment = Comment.objects.filter(active=True,video=video).order_by("-date")  #order by("-date") to get latest comments top
    # video=video means video that u are commenting and video that u watching should be match
    
    
    context = {
        "video": video,
        "comment":comment,
        "channel":channel,
    }
    return render(request,'video.html',context)


def channel_profile(request,id):
    channel =  Channel.objects.get(id=id)
    
    videos=Video.objects.filter(user=channel.user, visibility="public").order_by("-views")
    
    video_featured = Video.objects.get(user=channel.user.id) 
    
    context = {
        "channel":channel,
        "video_featured":video_featured,
        "videos":videos,
    }
    
    return render(request,"channel/channel.html",context)


def saved_video(request, id):
    video = Video.objects.get(id=id)
    user = Profile.objects.get(user=request.user)        # we want user profile, so we getting by user=request.user(it will current logged user)
    
    if video in user.saved_videos.all():
        user.saved_videos.remove(video)
    else:
        user.saved_videos.add(video)    
    
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))     #we are loading current page again, after clicking save button. HTTP REFERER is the header and (request.META.get("HTTP REFERER")) ->retreives url of current page from header
    


def ajax_save_comment(request):
    if request.method == "POST":
        pk= request.POST.get("id")    # this one is video id
        comment = request.POST.get("comment")
        video = Video.objects.get(id=pk)  # with video id we are getting actual video from DB
        user = request.user
        
        new_comment = Comment.objects.create(comment=comment,user=user,video=video)  #  this we are saving to DB.comment=comment - first one is database variable , second one is actual comment that we took from input
        new_comment.save()
        response="DONE"
        return HttpResponse(response)
         
@csrf_exempt         
def delete_comment(request):
    if request.method == "POST":
        id = request.POST.get("cid")   # comment id
        comment = Comment.objects.get(id=id)  # actual comment
        comment.delete()
        return JsonResponse({"status":1})
    else:
         return JsonResponse({"status":2})      
            
    
def add_new_subscribers(request, id):
        channel_subscribers = Channel.objects.get(id=id)    
        user = request.user
        
        if user in channel_subscribers.subscribers.all():        # channel_subscribers is channel and subscribers is subscribers of channel
            channel_subscribers.subscribers.remove(user)
            channel_subscribers.save() 
            response = "Subscribe"
            return JsonResponse(response,safe=False, status=200)
        else:
            channel_subscribers.subscribers.add(user)
            channel_subscribers.save() 
            response = "UnSubscribe"
            return JsonResponse(response,safe=False, status=200)
        
 
def load_channel_subs(request,id):
     channel_subscribers = Channel.objects.get(id=id)     
     sub_lists = list(channel_subscribers.subscribers.values())
     print("Subscribers List:", sub_lists)
     return JsonResponse(sub_lists, safe=False, status=200)
        
        
        

def add_new_like(request, id):
    video = Video.objects.get(id=id)
    user = request.user

    if user in video.likes.all():
        video.likes.remove(user)
        like_response = "Dislike"
    else:
        video.likes.add(user)
        like_response = "Like"

    return JsonResponse(like_response, safe=False, status=200)

def load_video_likes(request, id):
    video = Video.objects.get(id=id)
    likes_list = list(video.likes.values())
    return JsonResponse(likes_list, safe=False, status=200)
       
            
   
def add_new_dislike(request, id):
    video = Video.objects.get(id=id)
    user = request.user

    if user in video.dislikes.all():
        video.dislikes.remove(user)
        dislike_response = "Dislike"
    else:
        video.dislikes.add(user)
        dislike_response = "Like"

    return JsonResponse(dislike_response, safe=False, status=200)

def load_video_dislikes(request, id):
    video = Video.objects.get(id=id)
    dislikes_list = list(video.dislikes.values())
    return JsonResponse(dislikes_list, safe=False, status=200)        


def searchView(request):
    video = Video.objects.filter(visibility="public")
    query =  request.GET.get("qt")
    if query:
        video = video.filter(
            Q(title__icontains=query)|                       #comparing data base title with query
            Q(description__icontains=query)
        ).distinct()
        
    context ={
        "video":video,
        "query":query,
    }    
    return render(request,"search.html",context)