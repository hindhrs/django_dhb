document.addEventListener("DOMContentLoaded",()=>{
  const username=document.querySelector('#username');
  
if(username.textContent){
  Toastify({
    text: `Welcome back , ${username.textContent}`,
    duration: 3000, // Duration in milliseconds
    close: true, // Add a close button to the toast
    gravity: 'top', // Position of the toast on the screen
    position: 'right', // Position of the toast container
    backgroundColor: "linear-gradient(to right, #1c212c, #2c323e)", // Custom background color
    offset: {
      // Horizontal offset (right)
       x: 200 // Vertical offset (top)
   }
  }).showToast()
  
}else{
  console.log("no username to be displayed")
}
})


 function deleteItem(e) {

      icon=e.target
      const itemId = icon.dataset.itemId;
      fetch(`/delete-item/${itemId}/`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken')
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              // Remove the deleted item from the DOM
              // icon.closest('.row').remove();
              if(icon.classList.contains('ri-close-circle-line')){
                var tax=data.total_price*0.1;

                var grand_total=data.total_price+tax

                document.querySelector('.tax').textContent=`${tax} DH`

                document.querySelector('.grand-total').textContent=`${tax} DH`

                var total_price=document.querySelector('.sub-total')
                
                total_price.textContent=`${data.total_price} DH`;
                
                icon.closest(`.item-id-${itemId}`).remove();
                
                icon=document.querySelector(`.ri-close-line[data-item-id="${itemId}"]`)
              }
              icon.closest(`.row`).remove();
              total_price=document.querySelector('#cart-total')
              console.log(total_price)
              total_price.textContent=`${data.total_price} DH`;
              const productsCount=document.querySelector("#productsCount")
              productsCount.textContent=data.productsCount

          } else {
              // Handle error
              console.error('Failed to delete item');
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  };


 
document.querySelectorAll('.size-button').forEach(button => {
    button.addEventListener('click', function(e) {
       
        e.stopPropagation();
        const productId = button.dataset.productId;
        const size = button.textContent;
        const quantity=1
        addToCart(productId,size,quantity)
        // Call addToCart function here with productId and size
    });
});

  function addToCart(productId, size,quantity) {
    // Send AJAX request to Django server
    fetch('/add-to-cart/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken') // Ensure CSRF token is included
      },
      body: JSON.stringify({ productId: productId, size: size ,quantity:quantity})
    })
    .then(response => {
      console.log("1 then")
      return response.json();
    })
    .then(data=>{
      console.log('second then')
      const productsCount=document.querySelector("#productsCount")
      productsCount.textContent=data.productsCount+1
      console.log('productsCount updated')
      const product=data.product
      const item=data.item


      // Append the new cart item HTML to the existing cart items container
      const cartItemsContainer = document.querySelector(".offcanvas-body > div > div");
      cartItemsContainer.innerHTML += `
          <!-- Cart Product -->
          <div class="row mx-0 pb-4 mb-4 border-bottom">
              <div class="col-3">
                  <picture class="d-block bg-light">
                      <img class="img-fluid" src="/media/${product.img_path}.jpg" alt="${product.name}">
                  </picture>
              </div>
              <div class="col-9">
                  <div>
                      <h6 class="justify-content-between d-flex align-items-start mb-2">
                          ${product.name}
                          <i class="ri-close-line delete-item" data-item-id="${item.id}" onclick="deleteItem(event)"></i>
                      </h6>
                      <small class="d-block text-muted fw-bolder">Size: ${item.size}</small>
                      <small class="d-block text-muted fw-bolder">Qty: ${quantity}</small>
                  </div>
                  <p class="fw-bolder text-end m-0">${item.total_price} DH</p>
              </div>
          </div>
          <!-- /Cart Product -->
      `;

      total_price=document.querySelector('#cart-total')
      total_price.textContent=`${data.total_price} DH`;


      // Display toast message
  Toastify({
    text: data.message,
    duration: 2000, // Duration in milliseconds
    close: true, // Add a close button to the toast
    gravity: 'top', // Position of the toast on the screen
    position: 'right', // Position of the toast container
    backgroundColor: "linear-gradient(to right, #fc6229,#ffcd34)", // Custom background color
    offset: {
     // Horizontal offset (right)
      y: 42 // Vertical offset (top)
  }
  }).showToast();
    }
      )



    .catch(error => {
      console.error('Error:', error);
    });
  }

  // Function to get CSRF token from cookies
  function getCookie(name) {
   
    const value = `; ${document.cookie}`;
    
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  } 
