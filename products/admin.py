from django.contrib import admin

from products.models import ( 
    ProductType, Scenario, Question, Notification, Tool, RecognitionBoard, Promo,Troubleshoot
)

admin.site.register(ProductType)
admin.site.register(Scenario)
admin.site.register(Question)
admin.site.register(RecognitionBoard)
admin.site.register(Promo)
admin.site.register(Troubleshoot)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'resolved', 'updated_at']


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
