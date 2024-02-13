from django.contrib import admin

from cars.models import Brand, CarModel

admin.site.register(Brand)

admin.site.register(CarModel)