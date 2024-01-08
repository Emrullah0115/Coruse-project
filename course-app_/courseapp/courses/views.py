from datetime import date
import os
import random
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from courses.forms import CourseCreateForm, CourseEditForm,UploadForm
from .models import Course,Category, UploadModel
from django.core.paginator import Paginator
# Create your views here.

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"img2.jpg",
            "slug":"javascript-kursu",
            "date":date(2023,10,10),
            "isActive":True,
            "isUpdated":True,
        },
        {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"img1.jpg",
            "slug":"python-kursu",
            "date":date(2023,10,10),
            "isActive":False,
            "isUpdated":False,
        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"img3.jpg",
            "slug":"web-gelistirme-kursu",
            "date":date(2023,10,10),
            "isActive":True,
            "isUpdated":False,
        }
    ],
    "categories": [
        {"id": 1, "name": "programlama","slug":"programlama"},
        {"id": 2, "name": "web geliştirme","slug":"web-gelistirme"},
        {"id": 3, "name": "mobil uygulamalar","slug":"mobil-uygulamalar"},
    ]
}

def index(request):

    kurslar = Course.objects.filter(isHome=1,isActive=1)
    kategoriler = Category.objects.all()

    # for kurs in db["courses"]:
    #     if kurs["isActive"] == True:
    #         kurslar.append(kurs)

   

    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar
    })

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if not request.user.is_superuser:
        return redirect("index")
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/kurslar')
    else:
        form = CourseCreateForm()
       
    
    return render(request, "courses/create_course.html",{"form":form})

@login_required()
def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course-list.html',{
        'courses': kurslar
    })

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST,request.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render (request, "courses/edit-course.html", {
        "form":form
        })
    

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
    
      course.delete()
      return redirect("course_list")

    return render (request, "courses/course-delete.html", {"course":course})

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request,"courses/success.html")
    else:
        form = UploadForm()

    return render (request, "courses/upload.html",{"form":form})



def search(request):
   
    if "q" in request.GET and request.GET["q"] != "":
        q= request.GET["q"]
        kurslar=Course.objects.filter(isActive=True,title__contains=q,).order_by('date')
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    return render(request,'courses/search.html',{
       'categories': kategoriler,
        'courses': kurslar,
   }) 


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context={
         "course":course
    }
    return render(request,"courses/details.html", context)

def getCoursesByCategory(request, slug):
   
   kurslar=Course.objects.filter(categories__slug=slug,isActive=True).order_by("date")
   kategoriler = Category.objects.all()

   paginator = Paginator(kurslar, 2)
   page = request.GET.get('page',1)
   page_obj = paginator.page(page)

   print(page_obj.paginator.count)
   print(page_obj.paginator.num_pages)

   return render(request,'courses/list.html',{
       'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori':slug,
   }) 


