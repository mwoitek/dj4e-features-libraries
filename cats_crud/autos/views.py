from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from autos.forms import MakeForm
from autos.models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count()
        auto_list = Auto.objects.all()
        context = {'make_count': make_count, 'auto_list': auto_list}
        return render(request, 'autos/auto_list.html', context)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make_list = Make.objects.all()
        context = {'make_list': make_list}
        return render(request, 'autos/make_list.html', context)


class MakeCreate(LoginRequiredMixin, View):

    template = 'autos/make_form.html'

    # We use reverse_lazy() because we are in "constructor attribute" code that
    # is run before urls.py is completely loaded
    success_url = reverse_lazy('autos:all')


    def get(self, request):
        form = MakeForm()
        context = {'form': form}
        return render(request, self.template, context)


    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)
        # make = form.save()
        form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow. AutoUpdate
# (below) is doing the same thing with no code and no form by extending
# UpdateView.
class MakeUpdate(LoginRequiredMixin, View):

    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_form.html'


    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        context = {'form': form}
        return render(request, self.template, context)


    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)
        form.save()
        return redirect(self.success_url)


class MakeDelete(LoginRequiredMixin, View):

    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'


    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        context = {'make': make}
        return render(request, self.template, context)


    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


# Take the easy way out on the main table. These views do not need a form
# because CreateView, etc. build a form object dynamically based on the fields
# value in the constructor attributes.
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
