from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Subfolder, JSONFile
from .forms import SubfolderForm,JSONFileForm
from django.core.exceptions import ValidationError
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.contrib.auth.models import User


############################
#CRUD
############################

@login_required(login_url='/login')
def databag_view(request):
    ############################
    #Create
    ############################
    # username = request.user.username  
    # user = User.objects.get(username=username)
    
    if request.method == 'POST':
        form = SubfolderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            
            Subfolder.objects.create(user=request.user, name=name)
            return redirect('databag')
    else:
        form = SubfolderForm()

    ############################
    #retrieve
    ############################
    # subfolders_list = Subfolder.objects.filter(user=request.user).order_by('name')  # Order the subfolders by name
    # paginator = Paginator(subfolders_list, 5)  # Display 10 subfolders per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # context = {'form': form, 'page_obj': page_obj}
    # return render(request, 'dataApp/databag.html', context)
    
    query = request.GET.get('search', '')
    subfolders_list = Subfolder.objects.filter(Q(user=request.user) & Q(name__icontains=query)).order_by('name')
    paginator = Paginator(subfolders_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'page_obj': page_obj, 'search': query}
    return render(request, 'dataApp/databag.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def file_view(request, file_id):
    file = get_object_or_404(JSONFile, pk=file_id)
    context = {'file': file}
    return render(request, 'dataApp/file.html', context)

############################
#delete
############################
@login_required(login_url='/login')
def delete_subfolder(request, subfolder_id):
    subfolder = get_object_or_404(Subfolder, pk=subfolder_id)

    if request.method == 'POST':
        # Delete all files within the subfolder
        subfolder.jsonfile_set.all().delete()

        # Delete the subfolder itself
        subfolder.delete()

    return redirect('databag')

@login_required(login_url='/login')
def delete_file(request, file_id):
    file = get_object_or_404(JSONFile, pk=file_id)

    if request.method == 'POST':
        # Delete the file
        file.delete()

    return redirect('subfolder', subfolder_id=file.subfolder.id)

############################
#update
############################

@login_required(login_url='/login')
def edit_file(request, file_id):
    file = get_object_or_404(JSONFile, pk=file_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            json.loads(content)
            JSONFile.objects.filter(id=file_id).update(content=content)
            return redirect('subfolder', subfolder_id=file.subfolder.id)
        except json.JSONDecodeError:
            error_message = "Invalid JSON format"
            return render(request, 'dataApp/file.html', {'file': file, 'error_message': error_message})
    else:
        content = file.content

    return render(request, 'dataApp/file.html', {'file': file, 'content': content})