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

  window.fbAsyncInit = function() {
    FB.init({
      appId: '1511364552272668',
      cookie: true,
      xfbml: true,
      version: 'v2.11',
    });

    FB.AppEvents.logPageView();
  };

  (function(d, s, id) {
    let js,
      fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
      return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = 'https://connect.facebook.net/en_US/sdk.js';
    fjs.parentNode.insertBefore(js, fjs);
  })(document, 'script', 'facebook-jssdk');
});

const sendTokenToServer = () => {
  const { accessToken } = FB.getAuthResponse();
  console.log(accessToken);
  console.log('Welcome!  Fetching your information.... ');
  FB.api('/me', response => {
    console.log(`Successful login for: ${response.name}`);
    $.ajax({
      type: 'POST',
      url: '/fbconnect?state={{STATE}}',
      processData: false,
      data: accessToken,
      contentType: 'application/octet-stream; charset=utf-8',
      success(result) {
        // Handle or verify the server response if necessary.
        if (result) {
          $('#result').html(`Login Successful!</br>${result}</br>Redirecting...`);
          setTimeout(() => {
            window.location.href = '/';
          }, 4000);
        } else {
          $('#result').html('Failed to make a server-side call. Check your configuration and console.');
        }
      },
    });
  });
};
