from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import DeleteView

def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()

    def total_widgets():
        total = 0
        for widget in widgets:
            total += widget.quantity
        return total
    
    total = total_widgets()

    return render(request, 'home.html', { 'widgets': widgets, 'widget_form':widget_form, 'total_widgets': total })

def add_widget(request):
    if request.method == 'POST':
        widget_form = WidgetForm(request.POST)

        if widget_form.is_valid():
            new_widget = widget_form.save()
    
    return redirect('home')

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
