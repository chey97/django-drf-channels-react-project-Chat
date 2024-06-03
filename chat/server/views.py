from rest_framework.exceptions import ValidationError, AuthenticationFailed
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
        by_serverid = request.query_params.get("by_serverid")

        if (by_user or by_serverid) and not request.user.is_authenticated:
            raise AuthenticationFailed()

        if category:
            queryset = queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id
            queryset = queryset.filter(member=user_id)

        if qty:
            queryset = queryset[: int(qty)]

        if by_serverid:
            try:
                queryset = queryset.filter(id=by_serverid)
                if not queryset.exists():
                    raise ValidationError(
                        detail=f"Server with id {by_serverid} not found"
                    )
            except ValueError:
                raise ValidationError(detail=f"Server id {by_serverid} is not valid")

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)
