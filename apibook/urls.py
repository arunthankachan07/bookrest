
from django.contrib import admin
from django.urls import path
from .views import book_list,BookListView,BookDetailView,BookMixinView,\
    book_details,BookMixinDetail

urlpatterns = [
    path('books/', book_list,name="books"),
    path("books/<int:id>",book_details,name="bookdetails"),
    path('cbooks/',BookListView.as_view(),name="cbooks"),
    path('cbooks/<int:id>',BookDetailView.as_view(),name="detail"),
    path('mbooks/',BookMixinView.as_view(),name="mbooks"),
    path('mbooks/<int:pk>',BookMixinDetail.as_view(),name="mbooksdetail")

]