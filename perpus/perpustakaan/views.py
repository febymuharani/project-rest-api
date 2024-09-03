from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource

def export_xlsx(request):
    buku =  BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xlsx, content_type ='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="laporan buku.xlsx"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Di buat")
            return redirect('signup')
        else: 
            messages.error(request, "Terjadi Kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form
        }
    return render(request, 'signup.html', konteks)




@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('buku')


@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku
        }
    return render(request, template, konteks)



@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data Berhasil Di Tambah"
            konteks = {
                'form' : form,
                'pesan' : pesan
            }
            return render(request, 'tambah.html', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form' : form
        }

    return render(request, 'tambah.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # filter(kelompok_id__nama='Produktif')
    books = Buku.objects.all()
    konteks = {
        'books' : books
    }
    return render(request, 'buku.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def Penerbit(request):
    return render(request, 'penerbit.html')

