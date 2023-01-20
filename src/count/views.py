from django.shortcuts import redirect, render
from django.views import View

from count.forms import WordCountForm
from count.services import count_text


class HomeView(View):

    def get(self, request):
        return render(request, 'count/home.html')


class CountView(View):

    def get(self, request):
        form = WordCountForm()
        return render(request, 'count/counter_page.html', {'form_count': form})

    def post(self, request):
        form = WordCountForm(request.POST)
        if form.is_valid():
            total = count_text(form.cleaned_data['body'])
            return render(request, 'count/counter_page.html', {'total': total})

        return render(request, 'count/counter_page.html', {'form_count': form})