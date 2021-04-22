from rest_framework import serializers

from .models import ThongTinCaNhan, BanTin, BinhLuan


class ThongtincanhanSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThongTinCaNhan
        fields = '__all__'

class BantinviewsetSerializer(serializers.ModelSerializer):
    # TenNguoiPost = ThongTinCaNhan.objects.values('HoTen')
    class Meta:
        model = BanTin
        fields = '__all__'

class BantinSerializer(serializers.Serializer):
    IDBanTin = serializers.CharField(max_length=20)
    TenNguoiPost = ThongTinCaNhan.objects.values('HoTen')
    NoiDung= serializers.CharField(max_length=5000)

class BinhluanSerializers(serializers.ModelSerializer):

    class Meta:
        model = BinhLuan
        fields = '__all__'

