if (document.body.contains(document.getElementById("loginForm"))) {
  document
    .getElementById("loginForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;
      actions.actionLogIn(email, password);
    });

  document
    .getElementById("loginForm")
    .addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        event.preventDefault();
        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        actions.actionLogIn(email, password);
      }
    });
}
