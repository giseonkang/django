from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


# 회원가입
class UserCreateView(CreateView): 
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    #장고가내부포함하고있는 회원가입 폼클라스
    success_url = reverse_lazy('accounts:register_done') 
    #회원가입성공시 리다이렉트할링크
class UserCreateDoneView(TemplateView): 
    template_name = 'registration/register_done.html'




class writerOnlyMixin(AccessMixin):
    raise_exception = True 
    permission_denied_message = "User only can update/delete the object"


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.writer:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.writer:
            self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)



class StaffOnlyMixin(AccessMixin):
    raise_exception = True 
    permission_denied_message = "Staff only can update/delete the object"


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.staff:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)

class StaffOnlyDeleteMixin(AccessMixin):
    raise_exception = True 
    permission_denied_message = "Staff only can update/delete the object"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.staff:
            self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

# class customerOnlyMixin(AccessMixin):
#     raise_exception = True 
#     permission_denied_message = "Customer only can update/delete the object"

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if self.request.user != self.object.customer:
#             self.handle_no_permission()
#         return super().get(request, *args, **kwargs)