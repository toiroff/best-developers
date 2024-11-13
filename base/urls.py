from django.urls import path
from . import views

urlpatterns = [
  path('endpoints/',views.endpoint),
  path('advocates/',views.advocates_list,name="advocates"),
  path('advocates/<str:username>/',views.AdvocateDetail.as_view())
  # path('advocates/<str:username>',views.advocate_detail),
  
]