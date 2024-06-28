from django.urls import path
from .views import index
from .views import register,login
from .views import list_my_models,add_my_model
from .views import user_profile,search,get_mine,delete_remark,change_remark,logout_view
#from .views import password_reset_form,password_reset_email,password_reset_confirm,password_reset_complete
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/',login,name='login'),
    path('list/',list_my_models,name='list'),
    path('add/',add_my_model,name='add'),
    path('log_out/',logout_view,name='log_out'),
    path('user_profile/', user_profile, name='user_profile'),
    path('search_results/',search,name='search_results'),
    path('mine_remark/',get_mine,name='mine_remark'),
    path('delete_remark/<int:id>/',delete_remark,name='delete_remark'),
    path('change_remark/<int:id>/',change_remark,name='change_remark'),
]

# urls.py

