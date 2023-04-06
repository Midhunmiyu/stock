from django.urls import path
from . import views, adminviews, customerviews

urlpatterns = [
   path('',views.index,name='index'),
   path('login_view',views.login_view,name='login_view'),
   path('logout_view', views.logout_view, name='logout_view'),
   path('customer_registration',views.customer_registration,name='customer_registration'),

   #admin views
   path('admindashboard',adminviews.admindashboard,name='admindashboard'),
   path('Admin/Customerview',adminviews.view_customer,name='view_customer'),
   path('Admin/Stock/Add',adminviews.add_stock,name='add_stock'),
   path('Admin/Stock/View',adminviews.view_stock,name='view_stock'),
   path('Admin/Stock/delete/<int:id>/',adminviews.delete,name='delete'),


   #customer views
   path('customer_dashboard',customerviews.customer_dashboard,name='customer_dashboard'),
   path('customer/ViewStocks',customerviews.customer_View_stocks,name='customer_View_stocks'),

]
