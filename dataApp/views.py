from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Subfolder, JSONFile


#retrieve
def databag_view(request):
    subfolders = Subfolder.objects.all()

    paginator = Paginator(subfolders, 10)  # Display 10 subfolders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'dataApp/databag.html', context)

def subfolder_view(request, subfolder_id):
    subfolder = get_object_or_404(Subfolder, pk=subfolder_id)
    files_list = subfolder.jsonfile_set.all()
    
    paginator = Paginator(files_list, 10)  # Display 10 files per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'subfolder': subfolder, 'page_obj': page_obj}
    return render(request, 'dataApp/subfolder.html', context)

def file_view(request, file_id):
    file = get_object_or_404(JSONFile, pk=file_id)
    context = {'file': file}
    return render(request, 'dataApp/file.html', context)

