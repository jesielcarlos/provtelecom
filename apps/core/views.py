from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DetailView
from apps.callSystem.models import Called
from apps.core.models import Alerts
from apps.finance.models import Contas
from apps.profileUser.models import ProfileUser
from apps.services.models import ServicePlan
from django.views.generic import ListView


class HomeView(LoginRequiredMixin, View):
    template_name = "home.html"

    def get(self, request):
        ctx = {}
        profile = ProfileUser.objects.get(user=request.user)
        plans = ServicePlan.objects.filter(active=True).order_by('dt_created')[:3]
        contas = Contas.objects.filter(active=True, profile=profile).order_by('-dt_created')[:3]
        calleds = Called.objects.filter(active=True, profile=profile).order_by('-dt_created')[:3]
        alerts = Alerts.objects.filter(active=True, profile=profile).order_by('-dt_created')[:3]

        ctx['plans'] = plans
        ctx['contas'] = contas
        ctx['calleds'] = calleds
        ctx['alerts'] = alerts

        return render(request, self.template_name, ctx)


class ContractView(LoginRequiredMixin, ListView):
    model = ProfileUser
    template_name = 'contrato_impressao.html'

    def get_queryset(self):
        qs = ProfileUser.objects.filter(active=True)

        return qs