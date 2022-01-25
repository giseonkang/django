from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from accounts.views import StaffOnlyDeleteMixin, StaffOnlyMixin, writerOnlyMixin
from goods.forms import ReviewForm
from goods.models import Goods, Review
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.


# Goods

# PermissionRequiredMixin
class GoodsCreateView(LoginRequiredMixin,CreateView):
    model = Goods
    fields = ['name', 'thumbnail', 'goods_content', 'stock', 'price']
    template_name = 'goods/goods_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form): 
        form.instance.staff = self.request.user
        return super().form_valid(form)

class GoodsUpdateView(StaffOnlyMixin,UpdateView):
    model = Goods
    template_name = 'goods/goods_create.html'
    fields = ['name', 'thumbnail', 'goods_content', 'stock', 'price']
    success_url = reverse_lazy('home')


class GoodsDeleteView(StaffOnlyDeleteMixin,DeleteView):
    model = Goods
    success_url = reverse_lazy('home')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# class GoodsDetailView(FormMixin, DetailView):
#     model = Goods
#     form_class = ReviewForm(initial={'goods':Goods})
    



def goodsdetail(req, pk):   
    context ={}
    goods = get_object_or_404(Goods, pk=pk)
    reviews = Review.objects.filter(goods=pk)
    form = ReviewForm(initial={'goods':goods})
    context = {'goods' : goods, 'reviews' : reviews, 'form':form}
    return render(req, 'goods/goods_detail.html', context=context)


# Review
@login_required
def reviewcreate(req, pk):
    if req.method == 'POST':
        form = ReviewForm(req.POST)
        if form.is_valid():
            form.save(writer = req.user)
            pk = int(pk)
        return redirect('goods:detail' , pk)
    return Http404


class ReviewDeleteView(writerOnlyMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('home')
    # def delete(self, request, *args, **kwargs):
    #     """
    #     Call the delete() method on the fetched object and then redirect to the
    #     success URL.
    #     """
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)