from goods.views import GoodsCreateView, GoodsDeleteView, GoodsUpdateView, ReviewDeleteView, goodsdetail, reviewcreate
from django.urls import path

app_name = 'goods'

urlpatterns = [
    # path('', GoodsListView.as_view(), name='index'),

    path('detail/<int:pk>', goodsdetail, name='detail'),
    path('add/', GoodsCreateView.as_view(), name="add"),
    path('<int:pk>/update/', GoodsUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', GoodsDeleteView.as_view(), name="delete"),

    path('<int:pk>/reviewadd/', reviewcreate , name="review_add"), 
    path('<int:pk>/reviewdelete/', ReviewDeleteView.as_view(), name="review_delete"),
]
