from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.finance.models import Contas


class ContasView(LoginRequiredMixin, ListView):
    template_name ='contas_list.html'
    model = Contas

    def get_context_data(self, **kwargs):
        ctx = super(ContasView, self).get_context_data(**kwargs)

        if self.request.GET:
            contas = Contas.objects.filter(active=True)

            dt_start = self.request.GET.get('dt_start') 
            dt_end = self.request.GET.get('dt_end')

            if dt_start and dt_end:
                contas = contas.filter(active=True, dt_created__date__range=(dt_start,dt_end)).order_by('dt_created')

                ctx['contas'] = contas
                ctx['dt_start'] = dt_start
                ctx['dt_end'] = dt_end

        return ctx
