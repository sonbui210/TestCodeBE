from django.db import models
#sửa cái này để test git pull

# Create your models here.
class ThongTinCaNhan(models.Model):
    ChoiceGioiTinh = (
        ('Nam', 'Nam'),
        ('Nu', 'Nu'),
    )
    IDNguoiDung = models.CharField(max_length=20, null=False)
    TimeCreate = models.DateTimeField(auto_now=True)
    HoTen = models.CharField(max_length=80, null=False)
    GioiTinh = models.TextField(max_length=6, choices=ChoiceGioiTinh, default='')
    NgaySinh = models.DateField('Ngay Sinh')
    SDT = models.CharField(max_length=15, default=0, null=True)
    DiaChi = models.CharField(max_length=80, default='', null=True)

    def __str__(self):
        return self.IDNguoiDung

class BanTin(models.Model):
    IDBanTin = models.ForeignKey(ThongTinCaNhan, on_delete=models.CASCADE)
    # TenNguoiPost = ThongTinCaNhan.objects.values('HoTen')
    TenNguoiPost = models.CharField(max_length=20,  null=True)
    TimeCreateBanTin = models.DateTimeField(auto_now=True)
    NoiDung = models.CharField(max_length=5000, default='', null=True)
    # def __str__(self):
    # class Meta:
    #     ordering = 'Ten'
    #     return self.

class BinhLuan(models.Model):
    IDBinhLuan = models.ForeignKey(BanTin, on_delete=models.CASCADE)
    NguoiBinhLuan = models.CharField(max_length=80, null=False)
    NoiDungBinhLuan = models.CharField(max_length=5000, null=False)
    # def __str__(self):
    #     return self.IDBinhLuan
