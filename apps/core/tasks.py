from datetime import datetime
from celery import shared_task
from apps.core.models import Alerts
from apps.finance.models import Contas
from apps.profileUser.models import ProfileUser


@shared_task
def generate_contas():
 
    test_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day) 
    nxt_mnth = test_date.replace(day=28) + datetime.timedelta(days=4)
    res = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)
    
    profiles = ProfileUser.objects.filter(active=True)
    for profile in profiles:
        date = str(res.day)+'/'+str(datetime.now().month)+'/'+str(datetime.now().year)
        conta = Contas()
        conta.profile = profile
        conta.value = profile.service_plan.value
        conta.name = 'Conta - '+ profile.service_plan.name
        conta.dt_due = datetime.strptime(date, '%d/%m/%Y')
        conta.save()

        alert = Alerts()
        alert.profile = profile
        alert.title = 'Conta do mês gerada'
        alert.content = 'Conta referente ao mês atual criada - vencimento: '+ str(datetime.strptime(date, '%d/%m/%Y'))
        alert.save()

    return True

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
