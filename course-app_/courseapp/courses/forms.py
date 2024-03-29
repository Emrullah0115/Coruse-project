from django import forms
from courses.models import Course
# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Başlığı", 
#         required=True,
#         error_messages={
#         "required":"Kurs başlığı girmelisiniz."},
     
#     widget=forms.TextInput(
#         attrs=
#         {"class":"form-control"})

#     )
    

#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))



class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "image", "slug","isActive","isHome")
        label = {
            "title":"kurs başlığı",
            "description":"kurs açıklaması",
            "slug":"kurs slug"
            
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control",}),
            
        }
        error_messages = {
            "title": {
                    "required": "Kurs Başlığını girmelisiniz",
                    "maxlength": "maksimum 50 karakter"
            },
             "description": {
                    "required": "Kurs açıklamasını girin",
                    "maxlength": "maksimum 50 karakter"
            }
        }
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "image", "slug","categories","isActive","isHome")
        label = {
            "title":"kurs başlığı",
            "description":"kurs açıklaması",
            "slug":"kurs slug"
            
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control",}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
              
            
        }
        error_messages = {
            "title": {
                    "required": "Kurs Başlığını girmelisiniz",
                    "maxlength": "maksimum 50 karakter"
            },
             "description": {
                    "required": "Kurs açıklamasını girin",
                    "maxlength": "maksimum 50 karakter"
            }
        }   


class UploadForm(forms.Form):
    image = forms.ImageField()