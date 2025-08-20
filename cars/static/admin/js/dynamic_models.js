(function ($) {
    'use strict';
    $(document).ready(function () {
        var modelSelect = $('#id_model');
        var brandSelect = $('#id_brand');

        function updateModelOptions() {
            var brandId = brandSelect.val();
            if (brandId) {
                // Сохраняем текущее значение модели
                var currentModel = modelSelect.val();

                // Получаем новый URL с параметром brand
                var currentUrl = window.location.pathname;
                var newUrl = currentUrl + '?brand=' + brandId;

                // Перезагружаем страницу с новым параметром
                window.location.href = newUrl;
            } else {
                modelSelect.empty();
                modelSelect.append($('<option></option>').attr('value', '').text('---------'));
            }
        }

        brandSelect.on('change', function () {
            updateModelOptions();
        });
    });
})(django.jQuery);