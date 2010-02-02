$(function () {
    CKEDITOR.replaceAll(function(textarea, config) {
        if (textarea.className != "django-ckeditor") return false;
        
        config.toolbar =  [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize'
            ],
            [      'HorizontalRule',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'Cut','Copy','Paste','PasteText','PasteFromWord',
              '-', 'SpecialChar',
              '-', 'Source',
              '-', 'About'
            ]
        ];
        config.width = 840;
        config.height = 300;
        config.toolbarCanCollapse = false;
        
        return true;
    });
});