from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
from rest_framework.response import Response


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        # Start with all Server objects
        queryset = Server.objects.all()

        category = request.query_params.get("category")
        qty = request.query_params.get("qty")

        if category:
            queryset = queryset.filter(category__name=category)

        if qty:
            queryset = queryset[: int(qty)]

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)
