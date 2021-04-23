"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views  import add_items1
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('home/',views.home1,name="home1"),
    path('report/',views.reports,name="report"),
    path('contact/', views.contact),
    path('templateTagsDemo/', views.templateTagsDemo),
    path('search.html',views.search),
    path('Add/',views.Add,),
    path('bill/',views.bill,name='createbill'),
    path('list_items/',views.list_items,name='list_items'),
    path('add_items/',add_items1,name='Add'),
    path('update_items/<str:pk>',views.update_items,name='update_items'),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="myApp/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="myApp/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="myApp/reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="myApp/password_reset_done.html"),name="password_reset_complete"),
    path('delete_items/<str:pk>', views.delete_items, name='delete_items'),
    path('delete/',views.delete,name='delete'),
    path('details/<str:pk>', views.details, name='details'),
    path('sell_items/<str:pk>/',views.sell_items,name="sell_items"),
    path('purchase_items/<str:pk>/',views.purchase_items,name="purchase_items"),
    path('reorder/<str:pk>',views.reorder_level,name='reorder'),
    path('pdf_download/',views.DownloadPdf.as_view(),name="download_pdf"),
    path('download/',views.download,name="download")

]

