from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, reverse

from django.views.generic import DetailView, CreateView, UpdateView
from .models import Profile
from .forms import EditProfileForm
from article.mixins import FormMessageMixin


class ProfileDetailView(DetailView):
    template_name = 'account/profile.html'
    model = Profile
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'


class ProfileUpdateView(FormMessageMixin, UpdateView):
    template_name = 'account/edit_profile.html'
    model = Profile
    form_class = EditProfileForm
    context_object_name = 'update_profile'
    pk_url_kwarg = 'profile_id'
    form_valid_message = 'Updated successfully!'

    def get_queryset(self):
        return Profile.objects.all()

    def get_success_url(self, *args, **kwargs):
        return reverse('profile', args=(self.object.id,))


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Create user
        created_user = form.save()
        # Create profile
        profile = Profile.objects.create(user=created_user)
        # Authenticate User
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('profile', profile.id)

