const base_url = new URL('http://127.0.0.1:8000')

const clearCartButton = document.querySelector('#clear_cart');
const itemIncreaseButtonsList = document.querySelectorAll('#item_increase');
const itemDecreaseButtonsList = document.querySelectorAll('#item_decrease');
const addItemButtonsList = document.querySelectorAll('#add_item');
const itemDeleteButtonsList = document.querySelectorAll('#item_delete');
const cartBody = document.querySelector('#cart_block');

$(function () {
  $(clearCartButton).click(() => {
    $.ajax({
      url: new URL('cart/cart_clear/', base_url),
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
        url: new URL(`cart/cart_add/${product_id}`, base_url),
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
        url: new URL(`/cart/cart_qty/${product_id}/increase`, base_url),
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
        url: new URL(`cart/cart_qty/${product_id}/decrease`, base_url),
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
        url: new URL(`cart/cart_delete/${product_id}/`, base_url),
        type: 'get',
        success: (data) => {
          location.reload();
        },
      });
    });
  });
});
