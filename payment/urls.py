from django.urls import path


from . import views


app_name='payment'
urlpatterns = [
    path('process/', views.payment_process
         , name='process'),
    path('canceled/', views.payment_done
         , name='done'),
    path('done/', views.payment_canceled
         , name='canceled'),
]
