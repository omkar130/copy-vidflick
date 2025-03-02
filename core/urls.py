from django.urls import path,include
from core import views


urlpatterns=[
    path("",views.intro,name="intro"),
    path("register/login/",views.registeruser,name="registeruser"),
    path("index/",views.index,name="index"),
    path("trend/",views.trend,name="trend"),
    
    path("watch/<int:pk>/",views.videoDetail, name="video-detail"),
    path("ajax-save-comment/", views.ajax_save_comment,name="save-comment"),
    path("delete-comment/", views.delete_comment,name="delete-comment"),
    
    path("add-sub/<int:id>/", views.add_new_subscribers,name="add-sub"),
    path("load-sub/<int:id>/", views.load_channel_subs,name="load-sub"),
    
    path("add-like/<int:id>/", views.add_new_like,name="add_like"),
    path("likes-load/<int:id>/", views.load_video_likes,name="likeLoad"),
    
    path("add-dislike/<int:id>/", views.add_new_dislike,name="add_dislike"),
    path("dislikes-load/<int:id>/", views.load_video_dislikes,name="dislikeLoad"),
    
    path("channel/<int:id>/",views.channel_profile,name="channel-profile"),
    
    path("saved-video/<int:id>/",views.saved_video,name="saved-video"),
    
    path("show-saved-video/",views.show_saved_video,name="show_saved_video"),
    
    path("video/search/",views.searchView,name="search-view"),
    
    path("liked-video/<int:id>/",views.liked_video,name="liked-video"),
    
    path("show-liked-video/",views.show_liked_video,name="show-liked-video"),
    
    path("subscriptions/<int:id>",views.subscriptions,name="subscriptions"),
    
    path("show_subscriptions/",views.show_subscriptions,name="show_subscriptions"),
]