from django.views.generic import TemplateView, ListView
from .models import User


# Create your views here.
class HomePageView(TemplateView):
	http_method_names = ['post', 'get']
	template_name = "users/user_list.html"

class UserView(ListView):
	model = User
	template_name = "users/users.html"