from django.urls import path
from channel import views

urlpatterns = [
    path("channel/<int:id>",views.channel_profile,name="channel-prof"),
    path("channel/<int:id>/video/",views.channel_videos,name="channel-videos"),
    path("channel/<int:id>/about/",views.channel_about,name="channel-about"),
    path("channel/create/video",views.video_upload,name="video-upload"),
    path("channel/edit/<video_id>/<channel_id>",views.video_edit,name="video-edit"),
]