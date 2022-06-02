from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DetailView
from django_weasyprint import WeasyTemplateResponseMixin
from apps.callSystem.models import Called
from apps.finance.models import Contas
from apps.profileUser.models import ProfileUser
from apps.services.models import ServicePlan


class HomeView(LoginRequiredMixin, View):
    template_name = "home.html"

    def get(self, request):
        ctx = {}
        profile = ProfileUser.objects.get(user=request.user)
        plans = ServicePlan.objects.filter(active=True).order_by('dt_created')
        contas = Contas.objects.filter(active=True, profile=profile).order_by('dt_created')
        calleds = Called.objects.filter(active=True, profile=profile).order_by('dt_created')

        ctx['plans'] = plans
        ctx['contas'] = contas
        ctx['calleds'] = calleds

        return render(request, self.template_name, ctx)


class ContractView(LoginRequiredMixin, WeasyTemplateResponseMixin, DetailView):
    pass