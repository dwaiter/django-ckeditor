window.Django_CKEditor_Configs = [];

(function() {
    var done = [];
    var InitCKEditors = function() {
        django.jQuery('.django-ckeditor').each(function(i, el) {
            var elid = django.jQuery(el).attr('id');
            if (elid.indexOf('__prefix__') == -1) {
                if (django.jQuery.inArray(elid, done) == -1) {
                    var config = null;
                    django.jQuery.each(window.Django_CKEditor_Configs, function(i, val) {
                        console.log('testing ' + elid + ' against ' + val.re_dammit);
                        if (val.re.test(elid)) {
                            config = val.config;
                            return false;
                        }
                    });
                    CKEDITOR.replace(elid, config);
                    done.push(elid);
                }
            }
        });
        setTimeout(InitCKEditors, 1000);
    };
    InitCKEditors();
})()
