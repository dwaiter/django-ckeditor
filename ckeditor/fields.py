from django.db import models
from django.contrib.admin import widgets as admin_widgets
from ckeditor import widgets as ckeditor_widgets


class HTMLField(models.TextField):
    """A string field for HTML content. It uses the CKEditor widget in forms."""

    def formfield(self, **kwargs):
        defaults = { 'widget': ckeditor_widgets.CKEditor }
        defaults.update(kwargs)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = ckeditor_widgets.AdminCKEditor

        return super(HTMLField, self).formfield(**defaults)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^ckeditor\.fields\.HTMLField"])
except ImportError:
    pass