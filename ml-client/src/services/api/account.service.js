import axios from 'axios';


const API_URL = process.env.REACT_APP_API_V1


const getUserInfo = (successcallback, errorcallback) => {
    const token = localStorage.getItem("accessToken");
    axios.get(`${API_URL}/account/info`, {
        headers: {
            "Content-Type": "multipart/form-data",
            "Authorization": "Bearer " + token,
        },
    })
    .then(response => {
        if(successcallback != null){
           successcallback(response);
        }
      })
      .catch(err => {
        if(errorcallback != null){
           errorcallback(err);
        }
      })
}
  
const register = (username, email, password) => {
  return axios.post(`${API_URL}/account/signup`, {
    username,
    email,
    password,
  });
};

const logout = () => {
  localStorage.clear();
};


export default {
  getUserInfo,
  register,
  logout
}