try:
    import simplejson as json
except ImportError:
    import json

from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


CKEDITOR_CONFIGS = dict((k, json.dumps(v)) for k, v in settings.CKEDITOR_CONFIGS.items())
FILEBROWSER_PRESENT = 'filebrowser' in getattr(settings, 'INSTALLED_APPS', [])


class CKEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs['attrs'] if 'attrs' in kwargs else {}
        attrs['class'] = 'django-ckeditor'
        kwargs['attrs'] = attrs
        
        if 'ckeditor_config' in kwargs:
            self.ckeditor_config = kwargs.pop('ckeditor_config')
        else:
            self.ckeditor_config = 'default'
        
        super(CKEditor, self).__init__(*args, **kwargs)
    
    def render(self, name, value, attrs=None, **kwargs):
        rendered = super(CKEditor, self).render(name, value, attrs)
        context = {
            'name': name,
            'config': CKEDITOR_CONFIGS[self.ckeditor_config],
            'filebrowser': FILEBROWSER_PRESENT,
        }
        return rendered +  mark_safe(render_to_string(
            'ckeditor/ckeditor_script.html', context
        ))
    
    class Media:
        js = (
            settings.MEDIA_URL.rstrip('/') + '/ckeditor/ckeditor/ckeditor.js',
        )
        css = {
            'screen': (
                settings.MEDIA_URL.rstrip('/') + '/ckeditor/css/grappelli.css',
            ),
        }
    


class AdminCKEditor(admin_widgets.AdminTextareaWidget, CKEditor):
    pass

