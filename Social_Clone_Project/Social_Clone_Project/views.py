from django.views.generic import TemplateView
from django.urls import reverse
from django.views import generic


class HomePage(TemplateView):
    template_name = "index.html"


class TestPage(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:all')


class ThanksPage(TemplateView):
    template_name = 'thanks.html'