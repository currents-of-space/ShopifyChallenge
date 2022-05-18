from django.shortcuts import render,redirect
from django.db import connection


# Create your views here.
def index(request):
    """
    Home page - displays all products and filter form.

    **Context**

    ``products``
        All products in the system.

    ``form``
        Instance of the filtering form.

    **Template:**

    :template:`home/index.html`
    """

    cursor = connection.cursor()
    cursor.callproc('extract_all_product')
    column = [col[0] for col in cursor.description]

    products = [dict(zip(column,row)) for row in cursor.fetchall()]
    # products = Product.objects.all()
    # form = FilterForm()
    # context = {'products': products, 'form': form}

    context = {'products': products}
    cursor.close()
    return render(request, 'home/index.html', context)

def toLogin(request):
    return redirect('login')

# index(1)