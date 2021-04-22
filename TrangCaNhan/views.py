from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet



from .serializers import ThongtincanhanSerializer, BantinSerializer, BinhluanSerializers, BantinviewsetSerializer
from .models import ThongTinCaNhan, BanTin, BinhLuan
# Create your views here.

class ThongtincanhanViewset(viewsets.ModelViewSet):
    queryset = ThongTinCaNhan.objects.all()
    serializer_class = ThongtincanhanSerializer

class BantinViewset(viewsets.ModelViewSet):
    queryset = BanTin.objects.all()
    serializer_class = BantinviewsetSerializer
    # datacanhan = ThongTinCaNhan.objects.all()

    # def create(self, request, *args, **kwargs):
    #     bantin = BantinviewsetSerializer(data=request.data)
    #     if not bantin.is_valid():
    #         return Response("Sai du lieu", status=status.HTTP_400_BAD_REQUEST)
    #     IDBanTin=bantin.data['IDBanTin']
    #     Thongtinnguoidung = ThongTinCaNhan.objects.get(IDNguoiDung=IDBanTin)
    #     TenNguoiPost=ThongTinCaNhan.HoTen.__getitem__(IDBanTin)
    #     # TenNguoiPost = bantin.data['TenNguoiPost']
    #     NoiDung=bantin.data['NoiDung']
    #     cs = BanTin.objects.create(IDBanTin=IDBanTin, NoiDung=NoiDung)
    #     return Response(data=[cs.id, cs.IDBanTin, cs.TenNguoiPost, cs.NoiDung], status=status.HTTP_200_OK)


# class BantinViewset(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = BanTin.objects.all()
#         serializer = BantinviewsetSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         bantin = BantinSerializer(data=request.data)
#         if not bantin.is_valid():
#             return Response("Sai du lieu", status=status.HTTP_400_BAD_REQUEST)
#         # id = bantin.data['id']
#         # TimeCreate = bantin.data['TimeCreate']
#         IDBantin = bantin.data['IDBanTin1']
#         NoiDung = bantin.data['NoiDung1']
#         TenNguoiPost = bantin.data['TenNguoiPost1']
#         # TenNguoiPost = ThongTinCaNhan.objects.get(IDNguoiDung=IDBantin)
#         bantin_ = BanTin.objects.create(id=id, TimeCreate=TimeCreate, IDBanTin=IDBantin, NoiDung=NoiDung, TenNguoiPost=TenNguoiPost)
#         return Response(data=[bantin_.IDBanTin], status=status.HTTP_200_OK)
#
#     def retrieve(self, request, pk=None):
#         queryset = BanTin.objects.all()
#         bantin = get_object_or_404(queryset,pk=pk)
#         serializer = BantinSerializer(bantin)
#         return Response(serializer.data)



