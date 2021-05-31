
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Book
from .serializers import BookSerializer,BookModelSerializer
from rest_framework.views import APIView
from rest_framework import mixins, generics


# Create your views here.
#normal serilaizer - function based view
@csrf_exempt
def book_list(request):
    if request.method=="GET":
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        data=data=JSONParser().parse(request)
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=400)
@csrf_exempt
def book_details(request,id):
    book=Book.objects.get(id=id)
    if request.method =="GET":
        serializer=BookSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method =="PUT":
        data=JSONParser().parse(request)
        serializer=BookSerializer(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.errors,status=400)

    elif request.method =="DELETE":
        book.delete()
        return JsonResponse({"msg":"deleted"})





#Model serializer - class based view
class BookListView(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookModelSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        serializer=BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

class BookDetailView(APIView):
    def get_object(self,id):
        return Book.objects.get(id=id)
    def get(self,request,id):
        book=self.get_object(id)
        serializer=BookModelSerializer(book)
        return JsonResponse(serializer.data, status=201)
    def put(self,request,id):
        book=self.get_object(id)
        serializer=BookModelSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.data,status=401)
    def delete(self,request,id):
        book=self.get_object(id)
        book.delete()
        return JsonResponse({"msg": "deleted"})


#mixins
class BookMixinView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class BookMixinDetail(generics.GenericAPIView,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

