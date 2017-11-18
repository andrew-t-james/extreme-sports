document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach($el => {
      $el.addEventListener('click', () => {
        // Get the target from the "data-target" attribute
        const { target } = $el.dataset;
        const $target = document.getElementById(target);

        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }
});

function signInCallback(authResult) {
  if (authResult.code) {
    // Hide the sign-in button now that the user is authorized
    $('#signinButton').attr('style', 'display: none');
    // Send the one-time-use code to the server, if the server responds, write a 'login successful' message to the web page and then redirect back to the main restaurants page
    $.ajax({
      type: 'POST',
      url: '/gconnect?state={{STATE}}',
      processData: false,
      data: authResult.code,
      contentType: 'application/octet-stream; charset=utf-8',
      success(result) {
        // Handle or verify the server response if necessary.
        if (result) {
          $('#result').html(`Login Successful!</br>${result}</br>Redirecting...`);
          setTimeout(() => {
            window.location.href = '/restaurant';
          }, 4000);
        } else if (authResult.error) {
          console.log(`There was an error: ${authResult.error}`);
        } else {
          $('#result').html('Failed to make a server-side call. Check your configuration and console.');
        }
      },
    });
  }
}
