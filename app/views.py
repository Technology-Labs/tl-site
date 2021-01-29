from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse
from .forms import *
from .models import Leads

# Create your views here.
def index(request):
    form = QuotationForm()
    context ={ "form": form
    }
    return render (request, 'site/index.html', context )

def quote(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')
    description = request.POST.get('description')
    Leads(name=name, email=email, description=description).save()
    
    return redirect(index)


#  def quote_request(request):
#     context ={
#         "form" : form,
#     }
#     if request.method == 'POST':
#         form = QuotationForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             description = form.cleaned_data['description']
#             lead = QuotationForm(name=name, email=email, description=description)
#             lead.save()
#             HttpResponseRedirect('index')
#         else:
#             form = QuotationForm()
#     return render (request, 'site/quoteform.html', context )

    
def blog_post(request):
    return render (request, 'site/blog_post.html',{} )