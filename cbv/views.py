from django.shortcuts import render
# from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from django.http import HttpResponse
from cbv.models import Company,Producets
from django.urls import reverse_lazy
from cbv.models import Company, Producets, LoanApplication

# Create your views here.
class myclass(View):
    def get(self,request):
        return HttpResponse("<h1>this is cvb in django</h1>")

# class homepage(TemplateView):
#     template_name = "home.html"

class AllCompanies(ListView):
    model = Company
    # template_name = "cvb/company_list.html"
    
class CompaniesDetails(DetailView):
    model = Company
    context_object_name = "company_detail"

class AddNewCompany(CreateView):
    model = Company
    fields ="__all__"

class AddProduct(CreateView):
    model = Producets
    fields = "__all__"
    success_url = reverse_lazy('companies')

class EditCompany(UpdateView):
    model = Company
    fields = ['name','ceo','est_yer']

# class DeleteCompany(DeleteView);
#     model = Company
#     fields = []

class EmiCalculator(View):
    def get(self, request ,pk):
        product = Producets.objects.get(pk=pk)
        return render(request,'cbv/emi.html',{'product':product})

    def post(self,request,pk):
        product = Producets.objects.get(pk=pk)
        car_price = float(product.price)
        down_payment = float(request.POST.get("down_payment"))
        tenure = int(request.POST.get("tenure"))

        if tenure in [1,2,3,5]:
            interest_rate = 12
        else:
            interest_rate = 10

        loan_amount = car_price - down_payment
        monthly_rate = interest_rate/12/100
        months = tenure * 12

        emi = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
        total_payment = emi * months
        total_interest = total_payment - loan_amount

        return render(request,"cbv/emi.html",{
            "product":product,
            "car_price":car_price,
            "down_payment":down_payment,
            "loan_amount":loan_amount,
            "tenure":tenure,
            "interest_rate":interest_rate,
            "emi":round(emi,2),
            "total_payment":round(total_payment , 2),
            "total_interest":round(total_interest , 2),
            })

class ApplyLoan(View):
    def post(self,request,pk):
        product = Producets.objects.get(pk=pk)
        application = LoanApplication.objects.create(
            product = product,
            down_payment = request.POST.get("down_payment"),
            loan_amount = request.POST.get("loan_amount"),
            tenure = request.POST.get("tenure"),
            interest_rate = request.POST.get("interest_rate"),
            emi = request.POST.get("emi"),
            total_payment = request.POST.get("total_payment"),
            total_interest = request.POST.get("total_interest"),
        )
        return render(request,"cbv/loan_applied.html",{'application':application})