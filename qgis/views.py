from django.shortcuts import render

def post_list(request):
    return render(request, 'qgis/post_list.html', {})
