document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const loginWithGoogleBtn = document.getElementById('login-with-google');
  
    loginForm.addEventListener('submit', function(event) {
      event.preventDefault(); 
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;
      console.log('Username:', username);
      console.log('Password:', password);
    });
  
    loginWithGoogleBtn.addEventListener('click', function() {
      console.log('Login with Google clicked');
    });
  });

  
  document.addEventListener('DOMContentLoaded', function() {
    const confirmPasswordInput = document.getElementById('confirm-password');
    const confirmPasswordCheck = document.getElementById('confirm-password-check');

    confirmPasswordInput.addEventListener('input', function() {
        const password = document.getElementById('password').value;
        const confirmPassword = confirmPasswordInput.value;

        if (confirmPassword.length === 0) {
            confirmPasswordCheck.innerHTML = '';
            return;
        }

        if (password === confirmPassword) {
            confirmPasswordCheck.innerHTML = '&#10004;';
            confirmPasswordCheck.style.color = 'green';
        } else {
            confirmPasswordCheck.innerHTML = '&#9888;';
            confirmPasswordCheck.style.color = 'red';
        }
    });
});


document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    if (username === "admin" && password === "admin") {
        var loginMessage = document.getElementById("login-message");
        loginMessage.textContent = "Admin Login Success";
        window.open("admin.html", "_blank");
    } else {
        var loginMessage = document.getElementById("login-message");
        loginMessage.textContent = "Login Success";
        window.open("home.html", "_blank");
    }
});
