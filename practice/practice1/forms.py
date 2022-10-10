from django.forms import ModelForm
from .models import ApplicationForm

class ApplicationInput(ModelForm):
    class Meta:
        model = ApplicationForm
        fields = '__all__'

#for superuser