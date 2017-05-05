from django.forms import ModelForm
from collection.models import Blogpost

class BlogForm(ModelForm):
    class Meta:
        model = Blogpost
        fields = ('title', 'body',)
