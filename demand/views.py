from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import *
from .Serializer import *


class uploadView(APIView):
    def post(self, request, format=None):
        serializer = DemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("上传成功了")
        return Response("上传失败了")


class lookupall(APIView):
    def get(self, request, format=None):
        demand = Demand.objects.all()
        demand_serializer = DemandSerializer(demand, many=True)
        return Response(demand_serializer.data)


class lookup0(APIView):
    def get(self, request, format=None):
        demand = Demand.objects.filter(status=0)
        demand_serializer = DemandSerializer(demand, many=True)
        return Response(demand_serializer.data)


class lookup1(APIView):
    def get(self, request, format=None):
        demand = Demand.objects.filter(status=1)
        demand_serializer = DemandSerializer(demand, many=True)
        return Response(demand_serializer.data)


class lookup2(APIView):
    def get(self, request, format=None):
        demand = Demand.objects.filter(status=2)
        demand_serializer = DemandSerializer(demand, many=True)
        return Response(demand_serializer.data)


class changeView(APIView):
    def post(self, request, format=None):
        id = request.data.get('id')
        demand = Demand.objects.filter(id=id).update(**request.data)
        return Response("更改成功了")


class deleteView(APIView):
    def post(self, request, format=None):
        id = request.data.get('id')
        demand = Demand.objects.filter(id=id).delete()
        return Response("删除成功了")
