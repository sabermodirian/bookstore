from  django.urls import path
from django.views.generic import TemplateView

from .views import HomePageView #== from pages.views import HomePageView

# class HomeView(TemplateView):  بجای این از خط 8 استفاده میکنیم :ترفند:
# 	template_name='home.html'

urlpatterns = [
	# path('home/', TemplateView.as_view(template_name='home.html'), name = 'home'),
	path('home/' ,view = HomePageView.as_view() , name = 'home')
]