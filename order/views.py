from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.http.response import Http404
from order.forms import OrderForm
from goods.models import Goods
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def ordercreate(req, pk):    
    context ={}
    goods = get_object_or_404(Goods, pk=pk)
    form = OrderForm(initial={'goods_id':goods})
    context = {'goods' : goods, 'form':form}
    return render(req, 'order/order_create.html', context=context)

@login_required
def order_create_approve(req):
    if req.method == 'POST':
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save(customer = req.user)
        return redirect('order:order_done')
    return Http404()

class OrderCreateDoneView(TemplateView):
    template_name = 'order/order_done.html'