from django.contrib import admin
from django.apps import apps

# Ye code CORE app ke saare models ko auto admin me le aayega
# Chahe naam Project ho ya Projects, Skill ho ya Skills - sab aa jayenge

app = apps.get_app_config('core')

for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass