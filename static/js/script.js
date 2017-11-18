(() => {
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

  // function getUserData() {
  //   FB.api('/me', response => {
  //     document.getElementById('response').innerHTML = `Hello ${response.name}`;
  //   });
  // }

  // window.fbAsyncInit = function() {
  //   // SDK loaded, initialize it
  //   FB.init({
  //     appId: '1511364552272668',
  //     xfbml: true,
  //     version: 'v2.2'
  //   });

  //   // check user session and refresh it
  //   FB.getLoginStatus(response => {
  //     if (response.status === 'connected') {
  //       // user is authorized
  //       // document.getElementById('loginBtn').style.display = 'none';
  //       getUserData();
  //     } else {
  //       // user is not authorized
  //     }
  //   });
  // };

  // // load the JavaScript SDK
  // (function(d, s, id) {
  //   let js,
  //     fjs = d.getElementsByTagName(s)[0];
  //   if (d.getElementById(id)) {
  //     return;
  //   }
  //   js = d.createElement(s);
  //   js.id = id;
  //   js.src = '//connect.facebook.com/en_US/sdk.js';
  //   fjs.parentNode.insertBefore(js, fjs);
  // })(document, 'script', 'facebook-jssdk');

  // // add event listener to login button
  // document.getElementById('loginBtn').addEventListener(
  //   'click',
  //   () => {
  //     // do the login
  //     FB.login(
  //       response => {
  //         if (response.authResponse) {
  //           // user just authorized your app
  //           // document.getElementById('loginBtn').style.display = 'none';
  //           getUserData();
  //           sendTokenToServer();
  //         }
  //       },
  //       {
  //         scope: 'email,public_profile',
  //         return_scopes: true
  //       }
  //     );
  //   },
  //   false
  // );

  // function sendTokenToServer() {
  //   const access_token = FB.getAuthResponse().accessToken;
  //   console.log(access_token);
  //   console.log('Welcome!  Fetching your information.... ');
  //   FB.api('/me', response => {
  //     console.log(`Successful login for: ${response.name}`);
  //     $.ajax({
  //       type: 'POST',
  //       url: '/fbconnect?state={{STATE}}',
  //       processData: false,
  //       data: access_token,
  //       contentType: 'application/octet-stream; charset=utf-8',
  //       success(result) {
  //         // Handle or verify the server response if necessary.
  //         if (result) {
  //           $('#result').html(`Login Successful!</br>${result}</br>Redirecting...`);
  //           setTimeout(() => {
  //             window.location.href = '/';
  //           }, 4000);
  //         } else {
  //           $('#result').html('Failed to make a server-side call. Check your configuration and console.');
  //         }
  //       }
  //     });
  //   });
  // }
})();
