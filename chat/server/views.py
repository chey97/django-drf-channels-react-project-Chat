from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
from rest_framework.response import Response


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        queryset = Server.objects.all()

        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user")

        if category:
            queryset = queryset.filter(category__name=category)
            
        if by_user:
            user_id = request.user.id
            queryset = queryset.filter(member=user_id)

        if qty:
            queryset = queryset[: int(qty)]

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)
