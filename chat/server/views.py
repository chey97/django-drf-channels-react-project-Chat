from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.shortcuts import render
from rest_framework import viewsets
from .models import Server, Category, Channel
from .serializers import ServerSerializer, CategorySerializer, ChannelSerializer
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from .schema import server_list_docs
from drf_spectacular.utils import extend_schema


class ChannelListViewSet(viewsets.ViewSet):
    queryset = Channel.objects.all()
    
    @extend_schema(responses=ChannelSerializer)
    def list(self, request):
        serializer = ChannelSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class CategoryListViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()
    # permission_classes = [IsAuthenticated]

    @server_list_docs
    def list(self, request):
        """
        Handles GET requests to list Server objects with various filtering options.

        Query Parameters:
        - category (str, optional): Filter servers by category name.
        - qty (int, optional): Limit the number of results returned.
        - by_user (str, optional): If "true", filter servers where the current user is a member.
        - by_serverid (str, optional): Filter by specific server ID.
        - with_num_members (str, optional): If "true", include the number of members in each server.

        Raises:
        - AuthenticationFailed: If the user is not authenticated and requests filtering by user or server ID.
        - ValidationError: If the server ID is not valid or no server with the given ID is found.

        Returns:
        - Response: A JSON response containing the serialized server data.
        """

        queryset = Server.objects.all()

        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # if (by_user or by_serverid) and not request.user.is_authenticated:
        #     raise AuthenticationFailed()

        if category:
            queryset = queryset.filter(category__name=category)

        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                queryset = queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()

        if with_num_members:
            queryset = queryset.annotate(num_members=Count("member"))

        if by_serverid:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()

            try:
                queryset = queryset.filter(id=by_serverid)
                if not queryset.exists():
                    raise ValidationError(
                        detail=f"Server with id {by_serverid} not found"
                    )
            except ValueError:
                raise ValidationError(detail=f"Server id {by_serverid} is not valid")

        if qty:
            queryset = queryset[: int(qty)]

        serializer = ServerSerializer(
            queryset, many=True, context={"num_members": with_num_members}
        )
        return Response(serializer.data)


