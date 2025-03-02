from django import forms
from core.models import Video
from .models import Channel

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video                        
        fields = ['video','image','title','description','tags','visibility']
    
    
class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel                        
        fields = ['channel_art','image','full_name','channel_name','description','keywords']    