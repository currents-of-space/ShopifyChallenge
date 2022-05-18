from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST
# from .forms import CreateUserForm, EditUserForm, ChangePasswordForm
from django.db import connection

# Create your views here.
def toRegister(request):
    return render(request,'account/registration_new.html')

def registerPage(request):
    uname = request.POST.get('username','')
    pwd1 = request.POST.get('pwd1','')
    pwd2 = request.POST.get('pwd2','')
    email = request.POST.get('email','')
    fname = request.POST.get('fname','')
    lname = request.POST.get('lname','')
    tel = request.POST.get('tel','')
    is_seller = request.POST.get('is_seller','')
    if pwd1 != pwd2:
        messages.add_message(request,messages.ERROR,'Invalid Confirmation Password! Please Check and input again.')
        return redirect('registration')
    if uname and pwd1 and email and fname and lname and is_seller == "False" :
        cur = connection.cursor()
        cur.callproc('user_register',(uname,pwd1,email,fname,lname))
        messages.add_message(request, messages.SUCCESS, 'User Register Successfull. Please Sign in.')
        cur.close()
        return redirect('login')
    elif uname and pwd1 and email and tel and fname and lname and is_seller == "True":
        cur1 = connection.cursor()
        cur1.callproc('seller_register', (uname, pwd1, email, tel, fname, lname))
        messages.add_message(request, messages.SUCCESS, 'Seller Register Successfull. Please Sign in.')
        cur1.close()
        return redirect('sellerlogin')
    else:
        messages.add_message(request, messages.ERROR, 'Please fill out all the blank to finish the registration.')
        return redirect('registration')






def loginPage(request):
    if request.session.get('user_name',None) != None:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('usernameForm')
        password = request.POST.get('passwordForm')
        cursor = connection.cursor()
        cursor.callproc('veri_user',[username,password])
        login_state = cursor.fetchall()[0][0]

        print(login_state)
        if login_state:
            request.session['user_name'] = username
            messages.add_message(request, messages.SUCCESS, 'Login Successfull!')
            cursor.close()
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Username OR password is incorrect')
            cursor.close()
    context = {}
    return render(request, 'account/login.html', context)






def sellerLogin(request):
    """
       Display a login page and handle user login.

       **Template:**

       :template:`account/sellerlogin.html`
       """
    if request.session.get('seller_name', None) != None:
        return redirect('index')
    if request.method == 'POST':
        sellername = request.POST.get('sellername')
        sellerpwd = request.POST.get('sellerpwd')
        cursor = connection.cursor()
        cursor.callproc('veri_seller',[sellername,sellerpwd])
        login_state = cursor.fetchall()[0][0]

        print(login_state)
        if login_state:
            request.session['seller_name'] = sellername
            messages.add_message(request, messages.SUCCESS, 'Login Successfull!')
            cursor.close()
            return redirect('displayOrders')
        else:
            messages.add_message(request, messages.ERROR, 'Username or Password is incorrect')
            cursor.close()
    context = {}
    return render(request, 'account/sellerlogin.html', context)


def logoutAction(request):
    request.session.flush()
    messages.add_message(request, messages.SUCCESS, 'Account has been Logout')
    return redirect('index')





def manage(request):
    """
    Displays a user personal iformation management page and handles for managing a user personal information.

    **Context**

    ``editProfileForm``
        An instance of a form to manage user personal information.

    ``editPasswordForm``
        An instance of a form to change a user password.

    **Template:**

    :template:`account/manage.html`

    """
    if request.session.has_key('user_name'):
        if request.method == 'POST':
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email_add = request.POST.get('email')
            if first_name and last_name and email_add:
                user_name = request.session['user_name']
                cursor2 = connection.cursor()
                cursor2.callproc('update_info',[user_name,email_add,first_name,last_name])
                messages.add_message(request, messages.SUCCESS, 'Profile was changed successfully',
                                     extra_tags='editProfile')
                cursor2.close()
            else:
                messages.add_message(request, messages.ERROR, 'Could not change profile', extra_tags='editProfile')
            return redirect('manage')
        else:
            return render(request, 'account/manage.html')
    elif request.session.has_key('seller_name'):
        if request.method == 'POST':
            first_name = request.POST.get('fname','')
            last_name = request.POST.get('lname','')
            email_add = request.POST.get('email','')
            tel = request.POST.get('tel','')
            if first_name and last_name and email_add and tel:
                seller_name = request.session['seller_name']
                cursor2 = connection.cursor()
                cursor2.callproc('update_seller_info',[seller_name,email_add,tel,first_name,last_name])
                messages.add_message(request, messages.SUCCESS, 'Profile was changed successfully',
                                     extra_tags='editProfile')
                cursor2.close()
            else:
                messages.add_message(request, messages.ERROR, 'Could not change profile', extra_tags='editProfile')
            return redirect('manage')
        else:
            return render(request, 'account/manage.html')
    else:
        messages.add_message(request, messages.ERROR, 'Please Login First!')
        return redirect('index')


def changePassword(request):
    """
    Change user password.

    **Template:**

    If success - redirects to the manage endpoint.
    If not success - renders the :template:`account/manage.html`

    """
    if not request.session.has_key('user_name'):
        messages.add_message(request, messages.ERROR, 'Please Login First!')
        return redirect('index')

    if request.method == 'POST':
        pass_new = request.POST.get('pwd_new')
        pass_conf = request.POST.get('pwd_conf')
        user_name = request.session['user_name']
        if pass_conf == pass_new:
            cursor3 = connection.cursor()
            cursor3.callproc('update_pwd',[user_name,pass_new])
            messages.add_message(request, messages.SUCCESS, 'Password was changed successfully',
                                 extra_tags='changePassword')
        else:
            messages.add_message(request, messages.ERROR, 'Confirm Password Not Match, Please Input Again',
                                 extra_tags='changePassword')
        return render(request, 'account/manage.html')
    else:
        return redirect('manage')




    #     form = ChangePasswordForm(data = request.POST, user = request.user)
    #     if form.is_valid():
    #         form.save()
    #         update_session_auth_hash(request, form.user)
    #         messages.add_message(request, messages.SUCCESS, 'Password was changed successfully', extra_tags='changePassword')
    #     editProfileForm = EditUserForm(instance = request.user)
    #     context = {'editProfileForm': editProfileForm, 'editPasswordForm': form}
    #     return render(request, 'account/manage.html', context)
    # else:



def supervisorLogin(request):
    request.session.flush()
    if request.session.get('supervisor',None) != None:
        return redirect('index')
    if request.method == 'POST':
        super_name = request.POST.get('super_name')
        super_pwd = request.POST.get('super_pwd')
        cursor = connection.cursor()
        cursor.callproc('veri_super',[super_name,super_pwd])
        login_state = cursor.fetchall()[0][0]
        cursor.close()
        if login_state:
            request.session['super_name'] = super_name
            messages.add_message(request, messages.SUCCESS, 'Welcome! %s'%super_name)
            return redirect('supervisor')
        else:
            messages.add_message(request, messages.ERROR, 'Username OR password is incorrect')
    context = {}
    return render(request, 'account/supervisorlogin.html', context)

def issue_report(request):
    if not (request.session.has_key('user_name') or request.session.has_key('seller_name')):
        messages.add_message(request, messages.ERROR, 'Please Login in First!')
        return redirect('login')

    if request.method == 'POST':
        if request.session.has_key('user_name'):
            user_name = request.session.get('user_name')
            seller_name = request.POST.get('seller_name')
            super_id = request.POST.get('super_id')
            report_content = request.POST.get('complain_content')
            if user_name and seller_name and super_id and report_content:
                cursor = connection.cursor()
                cursor.callproc('issue_report',[user_name,seller_name,super_id,report_content])
                cursor.close()
                messages.add_message(request, messages.SUCCESS,
                                     'Report Successfull! Supervisor will revise the report and process.')
                return redirect('report')
            else:
                messages.add_message(request, messages.ERROR, 'Please Fill all the Form!')
        elif request.session.has_key('seller_name'):
            seller_name = request.session.get('seller_name')
            user_name = request.POST.get('user_name')
            super_id = request.POST.get('super_id')
            report_content = request.POST.get('complain_content')
            if user_name and seller_name and super_id and report_content:
                cursor = connection.cursor()
                cursor.callproc('issue_report', [user_name, seller_name, super_id, report_content])
                cursor.close()
                messages.add_message(request, messages.SUCCESS, 'Report Successfull! Supervisor will revise the report and process.')
                return redirect('report')
            else:
                messages.add_message(request, messages.ERROR, 'Please Fill all the Form!')
        else:
            messages.add_message(request, messages.ERROR, 'Please Login in First!')
    return render(request, 'account/report.html')

def report_review(request):
    if not request.session.has_key('super_name'):
        messages.add_message(request, messages.ERROR, 'Insufficient Permission!')
        return redirect('index')

    super_name = request.session['super_name']
    cursor = connection.cursor()
    cursor.callproc('issue_fetch',[super_name])
    column = [col[0] for col in cursor.description]
    complain_list = [dict(zip(column, row)) for row in cursor.fetchall()]
    # order_list = cursor.fetchall()
    context = {'complain_list':complain_list}
    return render(request,'account/supervisor.html',context)

def user_deactivate(request):
    if not (request.session.has_key('user_name') or request.session.has_key('seller_name')):
        messages.add_message(request, messages.ERROR, 'Please Login in First!')
        return redirect('login')
    if request.session.has_key('user_name'):
        user_name = request.session.get('user_name','')
        cursor = connection.cursor()
        cursor.callproc('del_user',[user_name])
        cursor.close()
        messages.add_message(request, messages.SUCCESS, 'Account Has Been Successfully Deactivated!')
        del request.session['user_name']
    if request.session.has_key('seller_name'):
        seller_name = request.session.get('seller_name', '')
        cursor = connection.cursor()
        cursor.callproc('del_seller', [seller_name])
        cursor.close()
        messages.add_message(request, messages.SUCCESS, 'Successfully Deactivate!')
        del request.session['seller_name']
    return redirect('index')





