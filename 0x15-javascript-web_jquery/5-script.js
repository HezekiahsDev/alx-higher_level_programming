// Adds a list element to the list when the div#add_item is clicked

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
