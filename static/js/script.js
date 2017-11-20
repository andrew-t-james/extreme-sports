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

  // login for logout flow
  const logoutBtn = document.getElementById('logoutBtn');
  const flashMessage = document.getElementById('flashMessage');
  const deleteBtn = document.getElementById('delete');

  function disconnect() {
    logoutBtn.classList.add('is-loading');
    $.ajax({
      type: 'GET',
      url: '/disconnect',
      success(result) {
        // Handle or verify the server response if necessary.
        window.location.href = '/sports';
      },
    });
  }

  if (logoutBtn !== null) {
    logoutBtn.addEventListener('click', () => {
      console.log('working');
      disconnect();
    });
  }

  if (deleteBtn !== null) {
    deleteBtn.addEventListener('click', () => {
      flashMessage.classList.add('none');
    });
  }
})();
