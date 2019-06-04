from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework import authentication
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rest_framework_simplejwt.authentication import JWTAuthentication as simplejwt
from rest_framework_simplejwt import views as jwt_views


from .models import *
from .serializers import *
from .permissions import *
from .urls import *

# Create your views here.


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()


class UserCreate(generics.CreateAPIView):
    # authentication_classes = ()
    permission_classes = (LibrarianPermission, )
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        if user.has_perm(LibrarianPermission) or user.has_perm(HallManagerPermission):
            return super(UserCreate, self).post(self, request, *args, **kwargs)
        else:
            raise PermissionError('You can not create new users.')

    # def post(self, request):
    #     user = request.data
    #     serializer = UserSerializer(data=user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserChange(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (simplejwt, )
    permission_classes = (HallManagerPermission, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(dir(request))
        user = authenticate(request, username=username, password=password)
        if user:
            print('something')
            login(request, user)
            # return Response('Login success')
            return redirect('/login/api/token/', username=username, password=password)#'token_obtain_pair',
            # return reverse(jwt_views.TokenObtainPairView.as_view())
        else:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)


# class LogoutView(APIView):
#     permission_classes = ()

#     def get(self, request):
#         logout(request)
#         return Response('You were logouted.')


class UsersBook(generics.ListAPIView):
    def get_queryset(self):
        queryset = Book.objects.filter(readers__id=self.kwargs['pk'])
        return queryset

    serializer_class = BookSerializer
    # authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['pk'])
        # and not request.user.is_superuser
        # if not request.user == user.username :
        #     raise PermissionError('You can not see books of this user.')
        return super().get(request, *args, **kwargs)


class UserDetail(generics.RetrieveAPIView):
    # authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorList(generics.ListAPIView):
    permission_classes = ()
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorChange(generics.RetrieveAPIView):
    permission_classes = (LibrarianPermission,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksOfAuthor(generics.ListAPIView):
    def get_queryset(self):
        queryset = Book.objects.filter(author__id=self.kwargs['pk'])
        return queryset

    serializer_class = BookSerializer


class BooksOfCategory(generics.ListAPIView):
    def get_queryset(self):
        queryset = Book.objects.filter(categories__id=self.kwargs['pk'])
        return queryset

    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
