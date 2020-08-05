from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product
from .forms import NewProduct
from django.contrib import messages
# Create your views here.
def product(request):
	messages.success(request, f"these data are just dummy, the website is still underconstruction!")
	messages.success(request, f"please feel free to check it out, and we're gratefully waiting for your feedback")
	products = Product.objects.all()

	context={
	'products':products,

	}
	return render(request, 'products/products.html', context)

def newproduct(request):
	if request.method == 'POST':
		user=request.user   
		user=User.objects.get(username=user.username)
		name = request.POST['name']
		p_type = request.POST['p_type']
		price = request.POST['price']
		url = request.POST['url']
		prd = Product(p_type=p_type,
		        name=name,
		        price=price,
		        url=url,
		        
		    )

		prd.save()
		return redirect('products') 

	else:
	    form=NewProduct()
	    

	context={
	'form':form
	}
	return render(request, 'products/new_product.html', context)

def product_details(request, pk, *args,  **kwargs): 
    messages.success(request, f"these data are just dummy, the website is still underconstruction!")
    messages.success(request, f"please feel free to check it out, and we're gratefully waiting for your feedback")
    product = Product.objects.get(id=pk)

    if request.method=='POST':
        user=request.user
        if request.POST.get('reserve') == '':
            pk = request.POST.get('pk')
            reserve =Product.objects.get(id=pk)                
            if prd.is_reversed == None:
                prd.is_reversed = user
                prd.save()
                return redirect('products')
            else:
                messages.warning(request,f'this product is already reserved')
        elif request.POST.get('delete') == '':
            Product.objects.get(id=pk).delete()
            return redirect('products')


    context={
        'product':product,
        'pk':pk,
    }
    return render(request, 'products/product_detail.html', context, *args, **kwargs)