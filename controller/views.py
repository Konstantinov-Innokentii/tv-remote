from django.shortcuts import render

from controller.data_processor import channel_list,source_list,channel_quantity,max_page


# Create your views here.


def index(request):
    return render(request, 'controller/site.html',{"channel_list": channel_list,"source_list": source_list,
                                                   "max_page": max_page})


