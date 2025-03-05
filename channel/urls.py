from django.urls import path
from channel import views

urlpatterns = [
    path("channel/<int:id>",views.channel_profile,name="channel-prof"),
    path("channel/<int:id>/video/",views.channel_videos,name="channel-videos"),
    path("channel/<int:id>/about/",views.channel_about,name="channel-about"),
    path("channel/create/video",views.video_upload,name="video-upload"),
    path("channel/edit/<video_id>/<channel_id>",views.video_edit,name="video-edit"),
    path("channel/delete/<video_id>/<channel_id>",views.video_delete,name="video_delete"),
    
    path("channel/create_channel",views.channel_create,name="channel-create"),
    path("channel/edit_channel",views.channel_edit,name="channel_edit"),
    path("channel/delete",views.channel_delete,name="channel_delete"),
    path("channel/<int:id>/your_video/",views.your_videos,name="your_videos"),
]