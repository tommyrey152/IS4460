from django.shortcuts import render
from rest_framework import generics
from .models import Orders
from .serializer import OrdersSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


