from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db import connection
from django.utils import timezone


# Create your views here.

def displayOrders(request):
    """
    Displays each order confirmed by users.

    **Context**

    ``orders``
        All orders confirmed by users.

    **Template:**

    If user is staff then returns :template:`order/orders.html`.
    If user is not staff then redirets to the index endpoint.

    """
    seller_name = request.session['seller_name']
    cursor = connection.cursor()
    cursor.callproc('fetch_order',[seller_name])

    column = [col[0] for col in cursor.description]
    order_list = [dict(zip(column, row)) for row in cursor.fetchall()]
    # order_list = cursor.fetchall()
    context = {'order_list':order_list}
    return render(request,'order/orders1.html',context)


def confirmOrder(request):
    if request.method == 'POST':
        if request.session.has_key('cartItems'):
            sessionCartItems = request.session['cartItems']
            if len(sessionCartItems) > 0:
                # user_name = request.session['user_name']
                user_name = request.POST.get('buyername')
                to = request.POST.get('buyeremail')
                buyer_phone = request.POST.get('buyerphone')
                buyer_note = request.POST.get('buyernote')
                pay_method = request.POST.get('pay_method')
                # print(pay_method)
                if user_name and buyer_phone and pay_method:
                    for cartItem in sessionCartItems:
                        cursor = connection.cursor()
                        cursor.callproc('user_information',[request.session['user_name']])
                        uid = cursor.fetchall()[0][1]
                        cursor.close()

                        # print(create_time)
                        # product = get_object_or_404(Product, id=cartItem['id'])
                        cursor1 = connection.cursor()
                        cursor1.callproc('fetch_product', [cartItem['id']])
                        column = [col[0] for col in cursor1.description]
                        product = [dict(zip(column, row)) for row in cursor1.fetchall()][0]
                        cursor1.close()
                        cursor2 = connection.cursor()
                        cursor2.callproc('veri_cus',[uid])
                        cus_status = cursor2.fetchall()[0][0]
                        cursor2.close()
                        create_time = timezone.now().strftime("%Y-%m-%d")
                        if not cus_status:
                            cursor3 = connection.cursor()
                            cursor3.callproc('create_customer',[buyer_phone,to,create_time,uid])
                            cid = cursor3.fetchall()[0][0]
                            cursor3.close()
                        else:
                            cursor3 = connection.cursor()
                            cursor3.callproc('update_cus',[buyer_phone,to,uid])
                            cid = cursor3.fetchall()[0][0]
                            cursor3.close()
                        orderPrice = (product['productPrice'] * cartItem['quantity'])
                        cursor4 = connection.cursor()
                        cursor4.callproc('track_paymethod',[pay_method])
                        pid = cursor4.fetchall()[0][0]
                        print(pid)
                        cursor4.close()
                        context = {"user_name": user_name, "orderPrice": orderPrice, "orderId": 21}
                        htmlContent = render_to_string("email.html", context)
                        textContent = strip_tags(htmlContent)
                        email = EmailMultiAlternatives(
                            "Order confirmation",
                            textContent,
                            settings.EMAIL_HOST_USER,
                            [to]
                        )
                        # email.send()
                        cursor5 = connection.cursor()
                        cursor5.callproc('create_order',[create_time,cid,buyer_note,product['productId'],pid])
                        cursor5.close()
                        messages.add_message(request, messages.SUCCESS, 'Order has been accepted')

                        del request.session['cartItems']
                        return redirect('index')
                else:
                    messages.add_message(request, messages.ERROR, 'Please Fill Out all the Information！')
                    return redirect('viewOrder')
    return redirect('viewOrder')


# @login_required(login_url='login')
# def confirmOrder(request):
#     """
#     Confirms users orders.
#
#     **Template:**
#
#     If the confirmation is success then redirects to the index endpoint.
#     If the confirmation is not succes then redirect to the cart endpoint.
#     """
#     if request.method == 'POST':
#         if request.session.has_key('cartItems'):
#             sessionCartItems = request.session['cartItems']
#             if len(sessionCartItems) > 0:
#                 form = DeliveryAddressForm(request.POST)
#                 if form.is_valid():
#                     firstName = form.cleaned_data['firstName']
#                     lastName = form.cleaned_data['lastName']
#                     email = form.cleaned_data['email']
#                     # deliveryAddress = DeliveryAddress(firstName = firstName, lastName = lastName, email = email)
#                     # deliveryAddress.save()
#                     # order = Order(deliveryAddress = deliveryAddress)
#                     # order.save()
#                     # orderPrice = 0
#                     for cartItem in sessionCartItems:
#                         product = get_object_or_404(Product, id = cartItem['id'])
#                         orderPrice = orderPrice + (product.Price * cartItem['quantity'])
#                         orderElement = OrderElement(product = product, quantity = cartItem['quantity'], order = order)
#                         orderElement.save()
#                     context={"firstName": firstName, "orderPrice": orderPrice, "orderId": 21}
#                     htmlContent = render_to_string("email.html", context)
#                     textContent = strip_tags(htmlContent)
#                     email = EmailMultiAlternatives(
#                         "Order confirmation",
#                         textContent,
#                         settings.EMAIL_HOST_USER,
#                         [email]
#                     )
#                     email.send()
#                     messages.add_message(request, messages.SUCCESS, 'Order has been accepted')
#                     del request.session['cartItems']
#                     return redirect('index')
#
#     return redirect('viewOrder')