from django.views.generic import View
from django.shortcuts import render
from .models import Kydolex_Post, Kydolex_Post2, Kydolex_Post3, Kydolex_Post4, Kydolex_Post5
from django.views.generic import TemplateView
from .models import Kydolex_list_WebDesign,Kydolex_list_UIUX,Kydolex_list_Icon,Kydolex_list_3D,Kydolex_list_graphic,Kydolex_list_video,Kydolex_list_Photograth,Kydolex_list_Image,Kydolex_list_Blog

class Kydolex_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post.objects.order_by("-id")
        post_data2 = Kydolex_Post2.objects.order_by("-id")
        post_data3 = Kydolex_Post3.objects.order_by("-id")
        return render(request, 'kydolex_app/index.html', {
            'post_data': post_data,
            'post_data2': post_data2,
            'post_data3': post_data3,
        })


class Kydolex_Blog_View(View):
    def get(self, request, *args, **kwargs):
        post_data4 = Kydolex_Post4.objects.order_by("-id")
        return render(request, 'kydolex_app/blog.html', {
            'post_data4': post_data4,
        })


class Kydolex_About_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post2.objects.order_by("-id")
        return render(request, 'kydolex_app/about.html', {
            'post_data': post_data,
        })


class Kydolex_Service_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post2.objects.order_by("-id")
        return render(request, 'kydolex_app/service.html', {
            'post_data': post_data,
        })


class Kydolex_designlist_View(View):
    def get(self, request, *args, **kwargs):
        design_data = Kydolex_list_WebDesign.objects.order_by("-id")
        uxui_data = Kydolex_list_UIUX.objects.order_by("-id")
        icon_data = Kydolex_list_Icon.objects.order_by("-id")
        threeD_data = Kydolex_list_3D.objects.order_by("-id")
        graphic_data = Kydolex_list_graphic.objects.order_by("-id")
        video_data = Kydolex_list_video.objects.order_by("-id")
        photograth_data = Kydolex_list_Photograth.objects.order_by("-id")
        image_data = Kydolex_list_Image.objects.order_by("-id")
        blog_data = Kydolex_list_Blog.objects.order_by("-id")
        return render(request, 'kydolex_app/designlist.html', {
            'design_data': design_data,
            'uxui_data': uxui_data,
            'icon_data': icon_data,
            'threeD_data': threeD_data,
            'graphic_data': graphic_data,
            'video_data': video_data,
            'photograth_data': photograth_data,
            'image_data': image_data,
            'blog_data': blog_data,
        })


class Kydolex_Contact_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post2.objects.order_by("-id")
        return render(request, 'kydolex_app/contact.html', {
            'post_data': post_data,
        })


class Kydolex_none_View(View):
    def get(self, request, *args, **kwargs):
        design_data = Kydolex_list_WebDesign.objects.order_by("-id")
        return render(request, 'kydolex_app/none.html', {
            'design_data': design_data,
        })