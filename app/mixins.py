from django.shortcuts import render
from django.views.generic import DetailView,FormView,CreateView, UpdateView, DeleteView, ListView
from . import models
from django.urls import reverse_lazy

class UrlMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model.__name__

        context["create_url_name"]="{}_create".format(self.prefix)
        context["detail_url_name"]="{}_detail".format(self.prefix)
        context["update_url_name"]="{}_update".format(self.prefix)
        context["delete_url_name"]="{}_delete".format(self.prefix)
        context["list_url_name"]="{}_list".format(self.prefix)
        return context

class CommonDetailMixin(UrlMixin):
    template_name="commons/detail.html"

    def get_context_data(self, **kwargs):
        from django.forms.fields import Field as form_field
        from django.db.models.fields import Field as model_field

        context = super().get_context_data(**kwargs)
        
        def field_disp(field):
            value =  getattr(self.object, field.name)
            choices =  getattr(field, "choices")
            if choices:
                for v in choices:
                    if v[0] == value:
                        value = v[1]
            return (field.verbose_name, value)

        fields = []
        for field in self.model._meta.get_fields():
            if isinstance(field, form_field) or isinstance(field, model_field):
                fields.append(field_disp(field))
            else:
                pass
                # print("This object has {}".format(type(field)))
        context["fields"] = fields
        return context

class CommonListMixin(UrlMixin):
    template_name="commons/list.html"
    pass

class CommonFormMixin(UrlMixin):
    template_name="commons/form_as_table.html"

    def get_success_url(self):
        return reverse_lazy('{}_detail'.format(self.prefix), args = (self.object.id,))

class CommonDeleteMixin(CommonDetailMixin):
    template_name="commons/delete.html"
    
    def get_success_url(self):
        return reverse_lazy('{}_list'.format(self.prefix))