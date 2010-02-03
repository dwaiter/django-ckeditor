from django.conf import settings
from django.conf.urls.defaults import *


try:
    import simplejson as json
except ImportError:
    import json

custom_editor_config = dict(
    (k, json.dumps(v)) for k, v in settings.CKEDITOR_CONFIG.items()
)

urlpatterns = patterns('django.views.generic.simple',
    url(r'^init.js$', 'direct_to_template', {
        'template': 'ckeditor/init.js',
        'extra_context': {
            'custom_editor_config': custom_editor_config,
        },
    }),
)