from django.contrib import admin
from .models import Sneaker
from .forms import SneakerForm
# Register your models here.


class SneakerAdmin(admin.ModelAdmin):
    form = SneakerForm


admin.site.register(Sneaker, SneakerAdmin)
