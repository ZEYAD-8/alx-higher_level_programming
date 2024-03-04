// List, add, remove.

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    // $("UL.my_list").remove("li:last-child");
    $('UL.my_list').children().last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').children().remove();
    // $("UL.my_list").empty();
    // $("UL.my_list").remove();
    // All three of these work.
    // NOTE: The last one removes the entire list, not just the children.
  });
});
