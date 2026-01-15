from django import forms
from .models import UserWishes

class WisheForm(forms.ModelForm):
    
        class Meta:
            model = UserWishes
            fields = [
                'wish'
            ]