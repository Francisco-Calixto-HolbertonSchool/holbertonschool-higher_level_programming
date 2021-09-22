window.addEventListener('DOMContentLoaded', (arrowfunct) => {
  $('#btn_translate').on('click', function () {
    const lang = $('#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + lang, (data) => {
    $('#hello').text(data.hello);
    });
  });
});
