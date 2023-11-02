if (document.body.contains(document.querySelector(".menu_icon"))) {
  let menu_button = document.querySelector(".menu_icon");
  let return_button = document.querySelector(".return_icon");
  let menu = document.querySelector(".custom-sidebar");
  menu_button.addEventListener("click", function (event) {
    menu.classList.add("sidebar-active");
  });

  return_button.addEventListener("click", function (event) {
    menu.classList.remove("sidebar-active");
  });

  let popup = document.querySelector(".popup");
  var voteData = {
    id_voter: Number,
    id_candidate: Number,
    id_candidature: Number,
  };

  function showPopup(id_candidate, id_candidature) {
    voteData["id_candidate"] = id_candidate;
    voteData["id_candidature"] = id_candidature;
    popup.style.display = "block";
  }

  function closePopup() {
    popup.style.display = "none";
  }

  let confirm_button = document.getElementById("confirm-button");
  confirm_button.addEventListener("click", function (event) {
    actions_user.actionNewVote(voteData);
    closePopup();
  });

  function logOut() {
    actions.actionLogOut();
  }
}
document.addEventListener("DOMContentLoaded", async function () {
  voteData["id_voter"] = await actions.actionCheckLoggedIn();
});
