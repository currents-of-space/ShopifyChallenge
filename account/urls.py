from django.urls import path
from .views import  loginPage, logoutAction, manage, changePassword,sellerLogin,toRegister,registerPage,issue_report,supervisorLogin,report_review,user_deactivate
# from .views import toRegister,registerPage

urlpatterns = [
    # path('', loginPage, name='logininitial'),
    path('registration/', toRegister, name='registration'),
    path('registration/index/',registerPage,name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutAction, name='logout'),
    path('manage/', manage, name='manage'),
    path('change-password/', changePassword, name='changePassword'),
    path('sellerlogin/', sellerLogin, name='sellerlogin'),
    path('supervisorlogin/', supervisorLogin, name='supervisorlogin'),
    path('report/', issue_report, name='report'),
    path('supervisor/', report_review, name='supervisor'),
    path('deactivate/', user_deactivate, name='deactivate'),
]