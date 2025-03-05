from .models import Channel
from django.contrib.auth.models import User

def user_channel(request):
    if request.user.is_authenticated:
        try:
            channel = Channel.objects.get(user=request.user)
        except Channel.DoesNotExist:
            channel = None
    else:
        channel = None
        
    return {'channel': channel}
