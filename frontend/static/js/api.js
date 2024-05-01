let apiUrl = "http://127.0.0.1:8000";

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

const api = {
  async logInGetToken(username, password) {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);

    return axios.post(`${apiUrl}/login`, params);
  },
  async getMe(token) {
    return axios.get(`${apiUrl}/me`, authHeaders(token));
  },
  async new_vote(token, data) {
    return await axios.post(`${apiUrl}/vote`, data, authHeaders(token));
  },
  async getcandidates(token) {
    try {
      let response = await axios.get(
        `${apiUrl}/candidates`,
        authHeaders(token)
      );
      return response.data;
    } catch (error) {
      throw new Error("Error al obtener candidatos: " + error.message);
    }
  },
  async getcandidatures(token) {
    try {
      let response = await axios.get(
        `${apiUrl}/candidatures`,
        authHeaders(token)
      );
      return response.data;
    } catch (error) {
      throw new Error("Error al obtener candidatos: " + error.message);
    }
  },
  async getcandidate(token, id) {
    return axios.get(`${apiUrl}/users/${id}`, authHeaders(token));
  },
  async getvotes(token) {
    return axios.get(`${apiUrl}/votes`, authHeaders(token));
  },
  async getMain(token) {
    return axios.get(`${apiUrl}/main`, authHeaders(token));
  },
};
