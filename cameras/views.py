from django.shortcuts import render, get_object_or_404, redirect
from .models import CamerasProfile
from .forms import CamerasProfileForm

def list_cameras(request):
    cameras = CamerasProfile.objects.all()
    return render(request, 'cameras/acesso.html', {'cameras': cameras})

def camera_detail(request, camera_id):
    camera = get_object_or_404(CamerasProfile, id=camera_id)
    return render(request, 'cameras/acesso.html', {'camera': camera})

def add_camera(request):
    if request.method == "POST":
        form = CamerasProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_cameras')  # Supõe que você tem uma URL nomeada para a view list_cameras
    else:
        form = CamerasProfileForm()
    return render(request, 'cameras/acesso.html', {'form': form})