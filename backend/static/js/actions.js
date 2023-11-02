const actions = {
  async actionLogIn(username, password) {
    try {
      let response = await api.logInGetToken(username, password);
      let token = response.data.access_token;
      if (token) {
        saveLocalToken(token);
        actions.actionRouteLoggedIn();
      } else {
        await actions.actionLogOut();
      }
    } catch (e) {
      console.log(e);
      let error_contain = document.getElementById("error_contain");
      error_contain.classList.add("active");
      setTimeout(function () {
        error_contain.classList.remove("active");
      }, 2000);
      await actions.actionLogOut();
    }
  },
  async actionCheckLoggedIn() {
    let localToken = getLocalToken();
    if (!localToken) actions.actionRouteLogOut();
    else {
      actions.actionRouteLoggedIn();
      try {
        let response = await api.getMe(localToken);
        return response.data.id;
      } catch (e) {
        if (e.response.status === 403) actions.actionLogOut();
        return e;
      }
    }
  },
  async actionRemoveLogIn() {
    removeLocalToken();
  },
  async actionLogOut() {
    await actions.actionRemoveLogIn();
    await actions.actionRouteLogOut();
  },
  actionRouteLogOut() {
    if (!window.location.pathname.includes("/login"))
      window.location.href = "/login";
  },
  actionRouteLoggedIn() {
    if (
      window.location.pathname === "/login" ||
      window.location.pathname === "/" ||
      window.location.pathname === "/register"
    ) {
      window.location.href = "/main";
    }
  },
};

const actions_user = {
  async actionGetMain() {
    try {
      let response = await api.getMain(getLocalToken());
      let template = response.data;
      document.body.innerHTML = template;
    } catch (error) {
      console.error(error);
      return error;
    }
  },
  async actionGetCandidatures() {
    try {
      let response = await api.getcandidatures(getLocalToken());
      console.log(response);
      if (response) {
        return response;
      }
    } catch (error) {
      return error;
    }
  },
  async actionGetCandidates() {
    try {
      let response = await api.getcandidates(getLocalToken());
      if (response) {
        return response.data;
      }
    } catch (error) {
      return error;
    }
  },
  async actionGetCandidate(id) {
    try {
      let response = await api.getcandidate(getLocalToken(), id);
      if (response) {
        return response.data;
      }
    } catch (error) {
      return error;
    }
  },
  async actionNewVote(voteData) {
    try {
      let response = await api.new_vote(getLocalToken(), voteData);
      if (response) {
        wrapper = document.querySelector(".candidates_container");
        wrapper.innerHTML = response.data;
        return response.data;
      }
    } catch (e) {
      console.error(e);
      if (e.response.status === 403) actions.actionLogOut();
      else if (e.response.status === 409) {
        wrapper = document.querySelector(".candidates_container");
        wrapper.innerHTML = e.response.data;
      }
      return e;
    }
  },
};
