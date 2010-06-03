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
GRAPPELLI_PRESENT = 'grappelli' in getattr(settings, 'INSTALLED_APPS', [])
MEDIA_URL = getattr(
    settings, 'CKEDITOR_MEDIA_URL', '%s/ckeditor' % settings.MEDIA_URL.rstrip('/')
)

_CSS_FILE = 'grappelli.css' if GRAPPELLI_PRESENT else 'standard.css'

class CKEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs['class'] = 'django-ckeditor'
        kwargs['attrs'] = attrs

        self.ckeditor_config = kwargs.pop('ckeditor_config', 'default')

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
            MEDIA_URL.rstrip('/') + '/ckeditor/ckeditor.js',
        )
        css = {
            'screen': (
                MEDIA_URL.rstrip('/') + '/css/' + _CSS_FILE,
            ),
        }



class AdminCKEditor(admin_widgets.AdminTextareaWidget, CKEditor):
    pass

