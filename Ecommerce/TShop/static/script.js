$(document).ready(function() {
    // Global variables
    var cartItems = [];

    // Function to add an item to the cart
    function addItemToCart(item) {
        cartItems.push(item);
        updateCartUI();
    }

    // Function to update the cart UI
    function updateCartUI() {
        var cartList = $("#cart-items");
        cartList.empty();

        var totalPrice = 0;

        cartItems.forEach(function(item) {
            var listItem = $("<li>").text(item.name + " - $" + item.price);
            cartList.append(listItem);

            totalPrice += item.price;
        });

        var totalElement = $("<li>").text("Total: $" + totalPrice.toFixed(2));
        cartList.append(totalElement);

        // Update cart item count in the navigation bar
        $("#cart-item-count").text(cartItems.length);
    }

    // Event listener for adding items to the cart
    $(".add-to-cart").click(function(event) {
        event.preventDefault();
        var itemName = $(this).data("name");
        var itemPrice = $(this).data("price");
        addItemToCart({ name: itemName, price: itemPrice });

        // Debugging: Log the data before and after storing it in Local Storage
        console.log("Data to store:", cartItems);

        // Store selected products in Local Storage
        localStorage.setItem("cartItems", JSON.stringify(cartItems));

        console.log("Stored data:", JSON.parse(localStorage.getItem("cartItems")));

        // Navigate to the cart.html page
        window.location.href = "cart.html";
    });

    // Retrieve selected products from Local Storage
    var storedCartItems = JSON.parse(localStorage.getItem("cartItems"));

    // Debugging: Log the retrieved data to the console
    console.log("Retrieved data:", storedCartItems);

    // Display the selected products in the cart
    if (storedCartItems) {
        var cartList = $("#cart-items");
        var totalPrice = 0;

        storedCartItems.forEach(function(item) {
            var listItem = $("<li>").text(item.name + " - $" + item.price);
            cartList.append(listItem);

            totalPrice += item.price;
        });

        var totalElement = $("<li>").text("Total: $" + totalPrice.toFixed(2));
        cartList.append(totalElement);
    }

    // Rest of your code...
});

function changeMainImage(clickedImage) {
    // Get the src of the clicked smaller image
    var newSrc = clickedImage.src;

    // Get the main product image element
    var mainImage = document.getElementById("MainImg");

    // Change the src of the main product image
    mainImage.src = newSrc;
}
