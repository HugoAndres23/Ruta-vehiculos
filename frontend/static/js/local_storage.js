const getLocalToken = () => localStorage.getItem("token");

const saveLocalToken = (token) => localStorage.setItem("token", token);

const removeLocalToken = () => localStorage.removeItem("token");
