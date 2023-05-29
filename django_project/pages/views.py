from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get_template_names(self):
        return ["home.html"]
