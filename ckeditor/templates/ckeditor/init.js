$(function () {
    CKEDITOR.replaceAll(function(textarea, config) {
        if (textarea.className != "django-ckeditor") return false;
        
        {% for key, value in custom_editor_config.items %}
            config.{{ key }} = {{ value|safe }};
        {% endfor %}
        
        return true;
    });
});