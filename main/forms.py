from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import News, Car

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]

        def clean_title(self):
            title = self.cleaned_data["title"]
            return strip_tags(title)

        def clean_content(self):
            content = self.cleaned_data["content"]
            return strip_tags(content)
        
class CarForm(ModelForm) :
    class Meta :
        model = Car
        fields = ["name", "brand", "stock"]
