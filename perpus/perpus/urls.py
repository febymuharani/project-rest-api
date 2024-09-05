from django.contrib import admin
from django.urls import path, include
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from perpustakaan.viewset_api import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('kelompok', KelompokViewset)


urlpatterns = [
    path('api/', include(router.urls)),  
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', Penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku,name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku,name='hapus_buku'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup', signup, name='signup'),
    path('export/xlsx/', export_xlsx, name='export_xlsx'),

]
