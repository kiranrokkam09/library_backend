from .models import Book
from .serializers import BookSerializer,UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


class book_add(generics.CreateAPIView): #Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class book_view(generics.ListAPIView): #all
    permission_classes = [IsAuthenticated, AllowAny]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class book_update(generics.RetrieveUpdateAPIView):#all
    permission_classes = [IsAuthenticated,AllowAny]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class book_delete(generics.RetrieveDestroyAPIView):#Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class members_add_view(generics.ListCreateAPIView):#Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()

class members_delete(generics.RetrieveDestroyAPIView):#Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()

class members_owndelete(APIView):#member
    permission_classes = [IsAuthenticated,AllowAny]
    def delete(self, request):
        member=User.objects.get(id=self.request.user.id)
        member.delete()
        return Response({"message":"User deleted"},status=status.HTTP_200_OK)


