
// disabled this affects every button kunaal

// Add event listener to "Add to Cart" buttons
document.addEventListener("DOMContentLoaded", function() {
    const addToCartButton = document.getElementById("addToCart");
    
    addToCartButton.addEventListener("click", function() {
            // Add gift to cart logic here
            console.log("Gift added to cart!");
            alert('Gift Added to cart!!')
        });
    
});


/// Function to search gifts by their name or description (for home page)
function searchGifts() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const giftItems = document.getElementsByClassName("gift-item");
    
    for (let i = 0; i < giftItems.length; i++) {
        const giftName = giftItems[i].getElementsByClassName("gift-name")[0].textContent.toLowerCase();
        const giftDescription = giftItems[i].getElementsByClassName("gift-description")[0].textContent.toLowerCase();
        
        if (giftName.includes(input) || giftDescription.includes(input)) {
            giftItems[i].style.display = "";
        } else {
            giftItems[i].style.display = "none";
        }
    }
}

// Function to search cart items (for cart page)
function searchCart() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const cartItems = document.getElementsByClassName("cart-item");
    
    for (let i = 0; i < cartItems.length; i++) {
        const cartName = cartItems[i].getElementsByClassName("cart-name")[0].textContent.toLowerCase();
        
        if (cartName.includes(input)) {
            cartItems[i].style.display = "";
        } else {
            cartItems[i].style.display = "none";
        }
    }
}

// Function to remove items from the cart
function removeItem(button) {
    const row = button.closest("tr");
    row.remove();
}
