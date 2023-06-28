from rest_framework.views import APIView    
from rest_framework.response import Response

from apps.promocode.models import Promocode
from apps.promocode.serializers import PromocodeSerializer

class PromocodeView(APIView):
    def get(self, request):
        promocodes = Promocode.objects.all()
        serializer = PromocodeSerializer(promocodes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PromocodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        promocode = Promocode.objects.get(pk=pk)
        serializer = PromocodeSerializer(promocode, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        promocode = Promocode.objects.get(pk=pk)
        promocode.delete()
        return Response(status=204)
