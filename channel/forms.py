from django import forms
from core.models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video                        
        fields = ['video','image','title','description','tags','visibility']
    