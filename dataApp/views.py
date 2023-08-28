from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Subfolder, JSONFile
from .forms import SubfolderForm,JSONFileForm
from django.core.exceptions import ValidationError
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import sweetify
# from django.contrib.auth.models import User


############################
#CRUD
############################

@login_required(login_url='/login')
def databag_view(request):
    ############################
    #Create
    ############################
    
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
    show_div = True
    query = request.GET.get('search', '')
    subfolders_list = Subfolder.objects.filter(Q(user=request.user) & Q(name__icontains=query)).order_by('name')
    paginator = Paginator(subfolders_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'page_obj': page_obj, 'search': query, 'show_div': show_div}
    return render(request, 'dataApp/databag.html', context)

@login_required(login_url='/login')
def subfolder_view(request, subfolder_id):

    subfolder = get_object_or_404(Subfolder, pk=subfolder_id)

    ############################
    #Create
    ############################
    if request.method == 'POST':
        form = JSONFileForm(request.POST)
        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.subfolder = subfolder
            file_obj.save()
            sweetify.info(request, 'File Created!')
        else:
             sweetify.error(request, 'Invalid JSON format')
        
        return redirect('subfolder', subfolder_id=subfolder_id)
        
    else:
        form = JSONFileForm()

    ############################
    #retrieve
    ############################
    show_div = True
    query = request.GET.get('search', '')
    files_list = subfolder.jsonfile_set.filter(Q(name__icontains=query)).order_by('name')  # Order the files by name
    
    paginator = Paginator(files_list, 5)  # Display 5 files per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {'subfolder': subfolder, 'form': form, 'page_obj': page_obj, 'search': query, 'show_div': show_div}
    return render(request, 'dataApp/subfolder.html', context)

@login_required(login_url='/login')
def redirect_to_file(request, subfolder_id):
    form = JSONFileForm()
    return render(request, 'dataApp/create_file_form.html', {'subfolder_id' : subfolder_id, 'form': form})


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
            sweetify.info(request, 'File Updated!')
            return redirect('subfolder', subfolder_id=file.subfolder.id)
        except json.JSONDecodeError:
            # error_message = "Invalid JSON format"
            sweetify.error(request, 'Invalid JSON format')
            return render(request, 'dataApp/file.html', {'file': file})
    else:
        content = file.content

    return render(request, 'dataApp/file.html', {'file': file, 'content': content})

