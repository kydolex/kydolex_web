from django.views.generic import View
from django.shortcuts import render
from .models import Kydolex_Post, Kydolex_Post2, Kydolex_Post3, Kydolex_Post4, Kydolex_Post5
from django.views.generic import TemplateView


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
        post_data = Kydolex_Post5.objects.order_by("-id")
        return render(request, 'kydolex_app/designlist.html', {
            'post_data': post_data,
        })


class Kydolex_Rate_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post2.objects.order_by("-id")
        return render(request, 'kydolex_app/rate.html', {
            'post_data': post_data,
        })


class Kydolex_Contact_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post2.objects.order_by("-id")
        return render(request, 'kydolex_app/contact.html', {
            'post_data': post_data,
        })


class Kydolex_none_View(View):
    def get(self, request, *args, **kwargs):
        post_data = Kydolex_Post2.objects.order_by("-id")
        return render(request, 'kydolex_app/none.html', {
            'post_data': post_data,
        })
