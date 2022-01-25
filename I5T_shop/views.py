from django.views.generic.list import ListView
from goods.models import Goods

class HomeView(ListView):
    model = Goods
    template_name = 'home.html'