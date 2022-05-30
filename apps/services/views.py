from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.callSystem.models import Called
from django.contrib import messages
from apps.services.models import ServicePlan


class ServicePlanView(LoginRequiredMixin, ListView):
    template_name ='serviceplan_list.html'
    model = ServicePlan

    def get_context_data(self, **kwargs):
        ctx = super(ServicePlanView, self).get_context_data(**kwargs)

        if self.request.GET:
            services = ServicePlan.objects.filter(active=True)

            dt_start = self.request.GET.get('dt_start') 
            dt_end = self.request.GET.get('dt_end')

            if dt_start and dt_end:
                services = services.filter(active=True, dt_created__date__range=(dt_start,dt_end)).order_by('dt_created')

                ctx['services'] = services
                ctx['dt_start'] = dt_start
                ctx['dt_end'] = dt_end

        return ctx
