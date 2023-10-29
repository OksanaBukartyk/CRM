from django.shortcuts import render,  get_object_or_404, redirect
from .models import Buyer, Seller, Selling, Product
from django.contrib import messages
from .forms import BuyerForm, SellerForm, ProductForm, SellingForm

# Create your views here.


def home(request):
    return render(request, 'shop_site/home.html', {'buyers': Buyer.objects.all(),
                                                   'sellers': Seller.objects.all(),
                                                   'sellings': Selling.objects.all(),
                                                   'products': Product.objects.all()})


def about(request):
    return render(request, 'shop_site/about.html')




def buyers_list(request):
    buyer = Buyer.objects.all()
    return render(request, 'shop_site/buyers.html', context={'buyers': buyer})


def sellers_list(request):
    sellers = Seller.objects.all()
    return render(request, 'shop_site/sellers.html', context={'sellers': sellers})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'shop_site/products.html', context={'products': products})


def sellings_list(request):
    sellings = Selling.objects.all()
    return render(request, 'shop_site/sellings.html', context={'sellings': sellings})



def buyer_edit(request, id):
    buyer = get_object_or_404(Buyer, id=id)
    if request.method == 'GET':
        context = {'form': BuyerForm(instance=buyer), 'id': id}
        return render(request,'shop_site/edit_form.html',context)
    
    elif request.method == 'POST':
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дані про покупця успішно оновлено!')
            return redirect('buyers_list')
        else:
            messages.error(request, 'Помилка:')
            return render(request,'shop_site/edit_form.html',{'form':form, 'title' :'покупця'})
        

def seller_edit(request, id):
    seller = get_object_or_404(Seller, id=id)
    if request.method == 'GET':
        context = {'form': SellerForm(instance=seller), 'id': id}
        return render(request,'shop_site/edit_form.html',context)
    
    elif request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дані про продавця успішно оновлено!')
            return redirect('sellers_list')
        else:
            messages.error(request, 'Помилка:')
            return render(request,'shop_site/edit_form.html',{'form':form, 'title_name' :'продавця'})
        
def selling_edit(request, id):
    selling = get_object_or_404(Selling, id=id)
    if request.method == 'GET':
        context = {'form': SellingForm(instance=selling), 'id': id}
        return render(request,'shop_site/edit_form.html',context)
    
    elif request.method == 'POST':
        form = ProductForm(request.POST, instance=selling)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дані про продаж успішно оновлено!')
            return redirect('sellings_list')
        else:
            messages.error(request, 'Помилка:')
            return render(request,'shop_site/edit_form.html',{'form':form, 'title_name' :'продажу'}) 
        


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        context = {'form': ProductForm(instance=product), 'id': id}
        return render(request,'shop_site/edit_form.html',context)
    
    elif request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дані про продукт успішно оновлено!')
            return redirect('products_list')
        else:
            messages.error(request, 'Помилка:')
            return render(request,'shop_site/edit_form.html',{'form':form, 'title' :'продукту'}) 
        

def buyer_delete(request, id):
    buyer = get_object_or_404(Buyer, id=id)
    context = {'data': buyer.first_name+ ' ' + buyer.last_name, "title":"покупця", 'link': 'buyers_list'}    
    if request.method == 'GET':
        return render(request, 'shop_site/delete.html',context)
    elif request.method == 'POST':
        buyer.delete()
        messages.success(request,  'Дані успішно видалено.')
        return redirect('buyers_list')
    
def seller_delete(request, id):
    seller = get_object_or_404(Seller, id=id)
    context = {'data': seller.first_name+ ' ' + seller.last_name, "title":"продавця", 'link': 'sellers_list'}    

    if request.method == 'GET':
        return render(request, 'shop_site/delete.html',context)
    elif request.method == 'POST':
        seller.delete()
        messages.success(request,  'Дані успішно видалено.')
        return redirect('sellers_list')
    
def selling_delete(request, id):
    selling = get_object_or_404(Selling, id=id)
    context = {'data': selling.product, "title":"продажу", 'link': 'sellings_list'}    
    
    if request.method == 'GET':
        return render(request, 'shop_site/delete.html',context)
    elif request.method == 'POST':
        selling.delete()
        messages.success(request,  'Дані успішно видалено.')
        return redirect('sellings_list')
    
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'data': product.product_name, 'title': 'продукту', 'link': 'products_list'}    
    
    if request.method == 'GET':
        return render(request, 'shop_site/delete.html',context)
    elif request.method == 'POST':
        product.delete()
        messages.success(request,  'Дані успішно видалено.')
        return redirect('products_list')


def buyer_create(request):
    if request.method == 'GET':
        return render(request,'shop_site/edit_form.html',{'form': BuyerForm()})
    elif request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Покупець успішно доданий.')
            return redirect('buyers_list')
        else:
            messages.error(request, 'Помилки:')
            return render(request,'shop_site/edit_form.html',{'form':form})
        
def seller_create(request):
    if request.method == 'GET':
        return render(request,'shop_site/edit_form.html',{'form': SellerForm()})
    elif request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продавець успішно доданий.')
            return redirect('sellers_list')
        else:
            messages.error(request, 'Помилки:')
            return render(request,'shop_site/edit_form.html',{'form':form})

def selling_create(request):
    if request.method == 'GET':
        return render(request,'shop_site/edit_form.html',{'form': SellingForm()})
    elif request.method == 'POST':
        form = SellingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продаж успішно доданий.')
            return redirect('sellings_list')
        else:
            messages.error(request, 'Помилки:')
            return render(request,'shop_site/edit_form.html',{'form':form})

def product_create(request):
    if request.method == 'GET':
        return render(request,'shop_site/edit_form.html',{'form': ProductForm()})
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успішно доданий.')
            return redirect('products_list')
        else:
            messages.error(request, 'Помилки:')
            return render(request,'shop_site/edit_form.html',{'form':form})
        

def user_sellings(request):
    seller=Seller.objects.get(id = request.user.id)
    sellings = Selling.objects.filter(seller = seller.id)
    print(sellings)
    return render(request,'shop_site/sellings.html',{'sellings':sellings})