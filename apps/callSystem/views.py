from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.callSystem.forms import CalledForm
from apps.callSystem.models import Called
from django.contrib import messages
from django.views.generic import CreateView

from apps.profileUser.models import ProfileUser


class CalledView(LoginRequiredMixin, ListView):
    template_name ='called_list.html'
    model = Called

    def get_context_data(self, **kwargs):
        ctx = super(CalledView, self).get_context_data(**kwargs)

        if self.request.GET:
            calleds = Called.objects.filter(active=True)

            dt_start = self.request.GET.get('dt_start') 
            dt_end = self.request.GET.get('dt_end')

            if dt_start and dt_end:
                calleds = calleds.filter(active=True, dt_created__date__range=(dt_start,dt_end)).order_by('dt_created')

                ctx['calleds'] = calleds
                ctx['dt_start'] = dt_start
                ctx['dt_end'] = dt_end

        return ctx


class CalledCreateView(LoginRequiredMixin, CreateView):
    template_name ='called_form.html'
    model = Called
    form_class= CalledForm
    success_message = 'Chamado editado com sucesso'
    warning_message = 'Erro na edição do chamado'

    def get_context_data(self, **kwargs):
        ctx = super(CalledCreateView, self).get_context_data(**kwargs)
        return ctx

    def form_valid(self, form):
        called_form = form.save(commit=False)
        called_form.profile = ProfileUser.objects.get(user=self.request.user)
        called_form.save()
        messages.success(self.request, self.success_message)
        return redirect('called')
