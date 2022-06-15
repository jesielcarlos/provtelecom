from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.finance.models import Contas
from apps.profileUser.models import ProfileUser
from django.contrib import messages


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

class PaymentReceiptPrintView(LoginRequiredMixin, ListView):
    model = Contas
    template_name = 'payment_receipt_print.html'

    def get_context_data(self, **kwargs):
        ctx= {}
        pk = self.kwargs['pk'] 
        profile = ProfileUser.objects.get(user=self.request.user)
        conta = Contas.objects.filter(pk=pk, active=True, profile=profile, status=Contas.CLOSED)
        if not conta:
            messages.warning(self.request, 'Conta não possui comprovante de pagamento')
            return redirect('home')
            
        ctx['conta'] = conta

        return ctx

class ContaPrintView(LoginRequiredMixin, ListView):
    model = Contas
    template_name = 'conta_print.html'

    def get_context_data(self, **kwargs):
        ctx= {}
        pk = self.kwargs['pk'] 
        profile = ProfileUser.objects.get(user=self.request.user)
        conta = Contas.objects.filter(pk=pk, active=True, profile=profile, status=Contas.OPEN)
        if not conta:
            messages.warning(self.request, 'Conta fechada, não possui boleto pra ser impresso')
            return redirect('home')

        ctx['conta'] = conta
        
        return ctx
