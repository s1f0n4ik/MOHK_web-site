
from django import forms
from .models import Product
import json
import sys
import logging
from django.core.files.storage import FileSystemStorage
from datetime import datetime

class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    template_name = 'admin/forms/widgets/multiple_image_input.html'

    def format_value(self, value):
        if not isinstance(value, (list, tuple)):
            try:
                urls = json.loads(value)
                value = [url for url in urls]
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
        return [] if value is None else value
class MultipleImageField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImageInput(attrs={'accept': 'image/*'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ProductModelForm(forms.ModelForm):
    sub_images = MultipleImageField(label='Select files', required=False)
    class Meta:
        model = Product
        fields = "__all__"

    def save(self, commit=True):
        instance = super().save(commit=False)


        files = self.cleaned_data['sub_images']
        sub_images = []
        t = datetime.today().strftime('%Y/%m/%d')

        for file in files:
            FileSystemStorage(location=f'media/media/products/{t}').save(file.name, file)
            sub_images.append(f'media/products/{t}/{file.name}')

        instance.sub_images = json.dumps(sub_images)

        if commit:
            instance.save()
        return instance
