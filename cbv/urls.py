from django.urls import path
from cbv import views


urlpatterns = [
    path('',views.AllCompanies.as_view(),name='companies'),
    path('create',views.AddNewCompany.as_view(),name="create"),
    path('product/', views.AddProduct.as_view(), name='add_product'),
    path('edit/<int:pk>',views.EditCompany.as_view(),name="edit"),
    path('emi/<int:pk>',views.EmiCalculator.as_view(),name='emi'),
    path('apply-loan/<int:pk>',views.ApplyLoan.as_view(),name="apply_loan"),
    path('<int:pk>',views.CompaniesDetails.as_view(), name='company_detail'),
]