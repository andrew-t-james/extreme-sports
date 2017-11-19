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

  function disconnect() {
    logoutBtn.classList.add('is-loading');
    $.ajax({
      type: 'GET',
      url: '/disconnect',
      success(result) {
        // Handle or verify the server response if necessary.
        window.location.href = '/';
      },
    });
  }

  const logoutBtn = document.getElementById('logoutBtn');
  logoutBtn.addEventListener('click', () => {
    console.log('working');
    disconnect();
  });
})();
