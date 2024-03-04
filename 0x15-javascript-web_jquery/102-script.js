// Fetches the translation of hello from fourtonfish API.

$('document').ready(function () {
  function translation () {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello',
      data: { lang: $('INPUT#language_code').val() },
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }

  $('INPUT#btn_translate').click(translation);
});
