// Fetches the translation of hello from fourtonfish API.
// Responds when the button is clicked or when the enter key is pressed.

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

  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translation();
    }
  });
});
