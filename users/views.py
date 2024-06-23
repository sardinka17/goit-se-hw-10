from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from users.forms import SignUpForm


class SignUpView(View):
    template_name = 'users/signup.html'
    form_class = SignUpForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Registration successfully')

            return redirect(to='quotes:index')

        return render(request, self.template_name, {'form': form})
