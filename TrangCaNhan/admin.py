from django.contrib import admin
from .models import ThongTinCaNhan, BanTin, BinhLuan
# Register your models here.

class ThontincanhanAdmin(admin.ModelAdmin):
    list_display = ('IDNguoiDung', 'HoTen', 'GioiTinh', 'NgaySinh')


class BantinAdmin(admin.ModelAdmin):
    list_display = ('IDBanTin', 'TenNguoiPost', 'TimeCreate', 'NoiDung' )

class BinhluanAdmin(admin.ModelAdmin):
    list_display = ('IDBinhLuan', 'NguoiBinhLuan')

admin.site.register(ThongTinCaNhan, ThontincanhanAdmin)
admin.site.register(BanTin, BantinAdmin)
admin.site.register(BinhLuan, BinhluanAdmin)
