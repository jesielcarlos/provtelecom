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

        services = ServicePlan.objects.filter(active=True)


        ctx['services'] = services


        return ctx
