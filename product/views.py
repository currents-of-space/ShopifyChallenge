from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

# Create your views here.
def productDetails(request, id):
    if not request.session.has_key('user_name'):
        messages.add_message(request, messages.ERROR, 'Please Login First!')
        return redirect('index')

    cursor = connection.cursor()
    cursor.callproc('fetch_product',[id])
    column = [col[0] for col in cursor.description]
    product = [dict(zip(column, row)) for row in cursor.fetchall()]
    print(product)
    context = {'product': product[0]}
    cursor.close()
    return render(request, 'product/details.html', context)

def productUpload(request):
    if not request.session.has_key('seller_name'):
        messages.add_message(request, messages.ERROR, 'ACCESS DENIED! Please Login into Seller Account First!')
        return redirect('index')
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_info = request.POST.get('product_info')
        product_pic = request.FILES.get('product_pic')
        save_dir = "./static/images/%s.jpg"%(product_name)
        pic_dir = 'images/%s.jpg'%(product_name)
        product_cat = request.POST.get('product_category')
        if product_name and product_price and product_info and product_pic and product_cat:
            with open(save_dir,'wb') as f:
                for content in product_pic.chunks():
                    f.write(content)
            cursor1 = connection.cursor()
            cursor1.callproc('fetch_sellerid',[request.session['seller_name']])
            sid = cursor1.fetchall()[0][0]
            cursor1.close()
            cursor2 = connection.cursor()
            cursor2.callproc('add_product',[product_name,product_price,sid,product_cat,product_info,pic_dir])
            cursor2.close()
            messages.add_message(request, messages.SUCCESS, 'Product Release Successful!')
        else:
            messages.add_message(request, messages.ERROR, 'Product Release Fail! Please Check the form!')
            return redirect('index')

    return render(request,'product/uploadproduct.html')


