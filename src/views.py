from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from products.models import Notification, Question, Tool, RecognitionBoard, Promo


@method_decorator(login_required, name='dispatch')
class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        recent_notifications = Notification.objects.all()[1:4]
        featured_qns = Question.objects.filter(featured=True)[:5]
        tools = Tool.objects.all()
        promos = Promo.objects.all()
        boards = RecognitionBoard.objects.all()

        return render(request, self.template_name, {
            'notifications': recent_notifications, 
            'questions': featured_qns, 
            'tools': tools,
            'promos': promos,
            'boards': boards
        })