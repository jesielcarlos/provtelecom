from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.profileUser.models import ProfileUser


class HomeView(LoginRequiredMixin, View):
    template_name = "home.html"

    def get(self, request):
        ctx = {}
        theme = ProfileUser.objects.filter(user=request.user).first().theme_dark
        ctx["theme"] = theme
        return render(request, self.template_name, ctx)
