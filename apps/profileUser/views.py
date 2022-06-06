from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import UpdateView
from apps.profileUser.forms import ProfileUserForm
from apps.profileUser.models import ProfileUser


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name ='profile_form.html'
    model = ProfileUser
    form_class= ProfileUserForm
    success_message = 'Perfil editado com sucesso'

    def get_context_data(self, **kwargs):
        ctx = super(ProfileUpdateView, self).get_context_data(**kwargs)
        return ctx

    def form_valid(self, form):
        profile_form = form.save()
        messages.success(self.request, self.success_message)
        return redirect('profile', pk=self.get_object().pk)
