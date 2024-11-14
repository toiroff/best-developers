from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('',views.endpoint),
  path('advocates/',views.advocates_list,name="advocates"),
  path('advocates/<str:username>/', views.AdvocateDetail.as_view(), 
         name='advocate_detail'),

  #companies
  path('companies/',views.companies_list,name='companies'),

  #Auth
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
]