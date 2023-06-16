from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ProductVs(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=productMS(PQS,many=True)
        return Response(PSD.data)
    
    def create(self,request):
        PSD=productMS(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'success':'Product Created succesfully'})
        else:
            return Response({'Failed':'Product is not created'})
    
    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=productMS(SPO)
        return Response(SPD.data)

    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=productMS(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
        
    def partial_update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=productMS(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is Partially updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
        
    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})
    