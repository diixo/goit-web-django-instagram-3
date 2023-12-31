from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

@login_required
def logout_view(request):
    if request.method == 'GET':
        username = request.user.username
        logout(request)
        return render(request, "users/logout.html", {"username": username})
    redirect(to="app_instagram:root")

class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="app_instagram:root")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Welcome: {username}. Account was created successfully')
            return redirect(to="users:login")

        return render(request, self.template_name, {"form": form})
