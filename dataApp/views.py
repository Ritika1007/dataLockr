from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Subfolder, JSONFile
from .forms import SubfolderForm,JSONFileForm


############################
#CRUD
############################

def databag_view(request):
    ############################
    #Create
    ############################
    if request.method == 'POST':
        form = SubfolderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Subfolder.objects.create(name=name)
            return redirect('databag')
    else:
        form = SubfolderForm()

    ############################
    #retrieve
    ############################
    subfolders_list = Subfolder.objects.order_by('name')  # Order the subfolders by name
    paginator = Paginator(subfolders_list, 10)  # Display 10 subfolders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'page_obj': page_obj}
    return render(request, 'dataApp/databag.html', context)

def subfolder_view(request, subfolder_id):

    subfolder = get_object_or_404(Subfolder, pk=subfolder_id)
    files_list = subfolder.jsonfile_set.order_by('name')  # Order the files by name

    ############################
    #Create
    ############################
    if request.method == 'POST':
        form = JSONFileForm(request.POST)
        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.subfolder = subfolder
            file_obj.save()
            return redirect('subfolder', subfolder_id=subfolder_id)
    else:
        form = JSONFileForm()

    ############################
    #retrieve
    ############################
    paginator = Paginator(files_list, 10)  # Display 10 files per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'subfolder': subfolder, 'form': form, 'page_obj': page_obj}
    return render(request, 'dataApp/subfolder.html', context)


def file_view(request, file_id):
    file = get_object_or_404(JSONFile, pk=file_id)
    context = {'file': file}
    return render(request, 'dataApp/file.html', context)

