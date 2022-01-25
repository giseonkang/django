from order.views import OrderCreateDoneView, order_create_approve, ordercreate
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('<int:pk>', ordercreate , name='order'),
    path('orderapprove/', order_create_approve , name="order_approve"), 
    path('done', OrderCreateDoneView.as_view(), name='order_done'),
]
