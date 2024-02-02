const clearCartButton = document.querySelector('#clear_cart');
const itemIncreaseButtonsList = document.querySelectorAll('#item_increase');
const itemDecreaseButtonsList = document.querySelectorAll('#item_decrease');
const addItemButtonsList = document.querySelectorAll('#add_item');
const itemDeleteButtonsList = document.querySelectorAll('#item_delete');
const cartBody = document.querySelector('#cart_block');

$(function () {
  $(clearCartButton).click(() => {
    $.ajax({
      url: 'http://127.0.0.1:8000/cart/cart_clear/',
      type: 'get',
      dataType: 'html',
      success: (data) => {
        location.reload();
      },
    });
  });

  addItemButtonsList.forEach((element) => {
    element.addEventListener('click', () => {
      const product_id = element.value;
      $.ajax({
        url: `http://127.0.0.1:8000/cart/cart_add/${product_id}/`,
        type: 'get',
        success: (data) => {
          location.reload();
        },
      });
    });
  });

  itemIncreaseButtonsList.forEach((element) => {
    element.addEventListener('click', () => {
      const product_id = element.value;
      $.ajax({
        url: `http://127.0.0.1:8000/cart/cart_qty/${product_id}/increase`,
        type: 'get',
        dataType: 'html',
        success: (data) => {
          location.reload();
        },
      });
    });
  });

  itemDecreaseButtonsList.forEach((element) => {
    element.addEventListener('click', () => {
      const product_id = element.value;
      $.ajax({
        url: `http://127.0.0.1:8000/cart/cart_qty/${product_id}/decrease`,
        type: 'get',
        success: (data) => {
          location.reload();
        },
      });
    });
  });

  itemDeleteButtonsList.forEach((element) => {
    element.addEventListener('click', () => {
      const product_id = element.value;
      $.ajax({
        url: `http://127.0.0.1:8000/cart/cart_delete/${product_id}/`,
        type: 'get',
        success: (data) => {
          location.reload();
        },
      });
    });
  });
});
