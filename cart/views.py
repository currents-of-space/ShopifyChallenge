from django.shortcuts import render, redirect

from django.contrib import messages

from django.db import connection

# Create your views here.
# @login_required(login_url='login')
def addToOrder(request, id, quantity):
    """
    Adds an element with the specified id to the cart.

    **Template:**

    Redirects to the viewCart endpoint
    """
    if request.session.get('cartItems',None):
        del request.session['cartItems']

    cursor = connection.cursor()
    cursor.callproc('fetch_product',[id])
    column = [col[0] for col in cursor.description]

    product = [dict(zip(column, row)) for row in cursor.fetchall()]
    cursor.close()
    if 1:
        if request.session.has_key('cartItems'):
            cartItems = request.session['cartItems']
            found = False
            for item in cartItems:
                if item['id'] == id:
                    found = True
                    # item['quantity'] = item['quantity'] + quantity
                    item['quantity'] = quantity
            if found == False:
                cartItems.append({'id': id, 'quantity': quantity})
            request.session['cartItems'] = cartItems
        else:
            cartItems = [{'id': id, 'quantity': quantity}]
            request.session['cartItems'] = cartItems
    return redirect('viewOrder')


def viewOrder(request):
    if not request.session.get('user_name', None):
        messages.add_message(request, messages.ERROR, 'Please Login First!')
        return redirect('index')
    """
    Displays all elements existed in the cart.

    **Context**

    ``cartItems``
        An array of key-value pairs. It contains products and the corresponding quantities of products.

    ``deliveryCost``
        The shipping cost.

    ``deliveryAddressForm``
        Instance of the delivery address form.

    **Template:**

    :template:`cart/cart.html`
    """
    if request.session.has_key('cartItems'):
        cartItems = []
        sessionCartItems = request.session['cartItems']
        if len(sessionCartItems) > 0:
            for sessionItem in sessionCartItems:
                cursor = connection.cursor()
                cursor.callproc('fetch_product', [sessionItem['id']])
                column = [col[0] for col in cursor.description]

                product = [dict(zip(column, row)) for row in cursor.fetchall()]
                cursor.close()
                # product = get_object_or_404(Product, id=sessionItem['id'])
                cartItem = {'product': product, 'quantity': sessionItem['quantity']}
                cartItems.append(cartItem)
        else:
            cartItems = None
    else:
        cartItems = None

    deliveryCost = "{:.2f}".format(0)
    # initial_dict = {
    #     # "firstName" : request.user.first_name,
    #     # "lastName" : request.user.last_name,
    #     # "email": request.user.email,
    #     "firstName": '',
    #     "lastName": '',
    #     "email": "",
    # }
    # deliveryAddressForm = DeliveryAddressForm(initial=initial_dict)
    # context = {'cartItems': cartItems, 'deliveryCost': deliveryCost, 'deliveryAddressForm': deliveryAddressForm}
    context = {'cartItems': cartItems, 'deliveryCost': deliveryCost}
    return render(request, 'cart/cart.html', context)


# @login_required(login_url='login')
# def viewOrder(request):
#     if not request.session.get('user_name',None):
#         messages.add_message(request, messages.ERROR, 'Please Login First!')
#         return redirect('index')
#     """
#     Displays all elements existed in the cart.
#
#     **Context**
#
#     ``cartItems``
#         An array of key-value pairs. It contains products and the corresponding quantities of products.
#
#     ``deliveryCost``
#         The shipping cost.
#
#     ``deliveryAddressForm``
#         Instance of the delivery address form.
#
#     **Template:**
#
#     :template:`cart/cart.html`
#     """
#     if request.session.has_key('cartItems'):
#         cartItems = []
#         sessionCartItems = request.session['cartItems']
#         if len(sessionCartItems) > 0:
#             for sessionItem in sessionCartItems:
#
#                 cursor = connection.cursor()
#                 cursor.callproc('fetch_product', [sessionItem['id']])
#                 column = [col[0] for col in cursor.description]
#
#                 product = [dict(zip(column, row)) for row in cursor.fetchall()][0]
#                 cursor.close()
#                 # product = get_object_or_404(Product, id = sessionItem['id'])
#                 cartItem = {'product': product, 'quantity': sessionItem['quantity']}
#                 cartItems.append(cartItem)
#         else:
#             cartItems = None
#     else:
#         cartItems = None
#
#     deliveryCost = "{:.2f}".format(0)
#     initial_dict = {
#         # "firstName" : request.user.first_name,
#         # "lastName" : request.user.last_name,
#         # "email": request.user.email,
#         "firstName" : '',
#         "lastName" : '',
#         "email": "",
#     }
#     deliveryAddressForm = DeliveryAddressForm(initial = initial_dict)
#     context = {'cartItems': cartItems, 'deliveryCost': deliveryCost, 'deliveryAddressForm': deliveryAddressForm}
#     return render(request, 'cart/cart.html', context)

# @login_required(login_url='login')
def removeFromCart(request, id):
    """
    Removes an item with the specified id from the cart.

    **Template:**

    Redirects to the "viewCart" endpoint.
    """
    if request.session.has_key('cartItems'):
        cartItems = request.session['cartItems']
        index = 0
        for cartItem in cartItems:
            if cartItem['id'] == id:
                cartItems.pop(index)
                request.session['cartItems'] = cartItems
                break
            index = index + 1

    return redirect('viewOrder')

# @login_required(login_url='login')
# def updateCartItemQuantity(request, id, quantity):
#     """
#     Updates the quantity of the product with the specified id.
#
#     **Template:**
#
#     Redirects to the "viewCart" endpoint.
#     """
#     if request.session.has_key('cartItems'):
#         cartItems = request.session['cartItems']
#         for cartItem in cartItems:
#             if cartItem['id'] == id:
#                 cartItem['quantity'] = quantity
#                 request.session['cartItems'] = cartItems
#                 break
#     return redirect('viewOrder')

