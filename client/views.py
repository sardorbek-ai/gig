from .forms import RegistrationForm
from django.views.generic import View
from django.shortcuts import render, redirect



class ClientRegistrations(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Ro'yxatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, _("Siz muvaffaqiyatli royxatdan o'tdingiz!"))
            return redirect('main:index')

        return render(request, 'layouts/form.html', {
            'form': form
        })
