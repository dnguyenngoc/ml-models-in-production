import axios from 'axios';

export const BASE_URL = process.env.REACT_APP_API_V1


export default function isAuth(){
    const freshToken = localStorage.getItem('freshToken');
    const accessToken = localStorage.getItem('accessToken');
    const isRemember = localStorage.getItem('isRemember');
    var expireAccessToken = localStorage.getItem('expireAccessToken');
    var expireFreshToken = localStorage.getItem('expireFreshToken');
    expireAccessToken = new Date(expireAccessToken)
    expireFreshToken = new Date(expireFreshToken)

    var d1 = new Date();
    var now = new Date( d1.getUTCFullYear(), d1.getUTCMonth(), d1.getUTCDate(), d1.getUTCHours(), d1.getUTCMinutes(), d1.getUTCSeconds() );
    const bodyFreshToken = new FormData();
    bodyFreshToken.append("refresh_token", freshToken);
    let check = false;

        
    if (accessToken === null) {check = false} // console.log('accessToken not on localStore!')
    else if (expireAccessToken > now) {check = true} // console.log("accessToken not expire yet!", expireAccessToken)
    else if (expireFreshToken < now) {return check} // console.log("freshToken expire!", expireFreshToken)
    else if (expireFreshToken > now && isRemember === 'true'){
        console.log("refreshToken not expire yet!", expireFreshToken)
        axios({
        method: "post",
        url: BASE_URL + "/account/login/refresh-token",
        data: bodyFreshToken,
        headers: { "Content-Type": "multipart/form-data" },
        }).then(function (response) {
            if (response.status === 200){
                check = true
                const data = response.data
                localStorage.setItem('tokenType', data.token_type)
                localStorage.setItem('accessToken', data.access_token)        
                localStorage.setItem('freshToken', data.refresh_token)   
                localStorage.setItem('expireAccessToken', data.expire_token)   
                localStorage.setItem('expireFreshToken', data.expire_refresh_token) 
                // console.log("new token create by fresh token!")
            }
            else {
                check = false
                localStorage.clear()
                // console.log("fresh error token")
            }
        }).catch(function (response) {
            check = false
            localStorage.clear();
            // console.log("api error token")
        });
    }else {
        check = false
        localStorage.clear();
        // console.log("khac")
    }
    // console.log("Auth:", check)
    return check
}