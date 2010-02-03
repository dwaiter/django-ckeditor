from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets


class CKEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs['attrs'] if 'attrs' in kwargs else {}
        attrs['class'] = 'django-ckeditor'
        kwargs['attrs'] = attrs
        super(CKEditor, self).__init__(*args, **kwargs)
    
    class Media:
        js = (
            settings.MEDIA_URL.rstrip('/') + '/ckeditor/ckeditor/ckeditor.js',
            '/ckeditor/init.js',
        )


class AdminCKEditor(admin_widgets.AdminTextareaWidget, CKEditor):
    pass

