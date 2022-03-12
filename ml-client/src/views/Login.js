
import React from 'react';
import CustomInput from "../components/input/CustomInput";
import Button from "../components/buttom/Buttom";
import axios from 'axios';
import { Alert } from 'antd';


export const BASE_URL = process.env.REACT_APP_API_V1


export default class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            email: "",
            password: "",
            isLogin: false,
            loading: false,
            isRemember: true,
            showAlert: false,
            alertDescription: '',
            makeLogin: false
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleLogin = this.handleLogin.bind(this)
    }

    handleChange = e => this.setState({ [e.currentTarget.id]: e.currentTarget.value })
    handleLogin(){this.setState({makeLogin: true})}

    handleAll = async () =>{
        if (this.state.isLogin === true) window.location.href = "/"
        else if (this.state.makeLogin === true) 
        {
            var bodyFormData = new FormData();
            bodyFormData.append('username', this.state.email);
            bodyFormData.append('password', this.state.password);
            let isRemember = this.state.isRemember;
            const result = await axios({
                method: "post",
                url: BASE_URL + "/account/login/access-token",
                data: bodyFormData,
                headers: { "Content-Type": "multipart/form-data" },
            })
                .then(function (response) {
                    if (response.status === 200){
                        const data = response.data
                        localStorage.setItem('isRemember', isRemember)
                        localStorage.setItem('tokenType', data.token_type)
                        localStorage.setItem('accessToken', data.access_token)        
                        localStorage.setItem('freshToken', data.refresh_token)   
                        localStorage.setItem('expireAccessToken', data.expire_token)   
                        localStorage.setItem('expireFreshToken', data.expire_refresh_token)
                        // if (!data.role_name.length) {localStorage.setItem('role', null)}
                        // else localStorage.setItem('role', data.role_name.map(t=>t).reduce((prev, curr) => [prev, curr]))
                        return {isLogin: true, alertDescription:'', showAlert: false}
                    }
                })
                .catch(function (response) {
                    console.log(response)
                    if (response.response === undefined) return {showAlert: true, alertDescription:'error from Server!', isLogin:false}
                    else if (response.response.status === 400) return {showAlert: true, alertDescription:'wrong email or password!', isLogin:false}
                    else if (response.response.status === 404) return {showAlert: true, alertDescription:'Not found User!', isLogin:false}
                    else if (response.response.status === 422) return {showAlert: true, alertDescription:'missing email or password!', isLogin:false}
                    else return {showAlert: true, alertDescription:'error from Server!', isLogin: false}
            });
            this.setState({makeLogin: false, isLogin: result.isLogin, showAlert: result.showAlert, alertDescription: result.alertDescription})
        }
    }
    componentDidUpdate(){this.handleAll()}
    componentDidMount(){
        const script = document.createElement("script");

        script.src = process.env.PUBLIC_URL + "/js/test.js";
        script.async = true;
    
        document.body.appendChild(script);
    }

    render() {
        return ( 
            <div className="login">
                {/* <div className='content--canvas'></div> */}
                <canvas id="canvas"></canvas>
                <form className="form">
                { this.state.showAlert ? <Alert message={this.state.alertDescription} type="warning" /> : ""}
                    <img className="logo" alt="logo" src ={process.env.PUBLIC_URL + '/img/logo.png'}></img>
                <CustomInput
                    labelText="Email"
                    id="email"
                    formControlProps={{
                    fullWidth: true
                    }}
                    handleChange={this.handleChange}
                    type="text"
                />
                <CustomInput
                    labelText="Password"
                    id="password"
                    formControlProps={{
                    fullWidth: true
                    }}
                    handleChange={this.handleChange}
                    type="password"
                />

                <Button type="button" color="primary" className="form__custom-button" onClick={this.handleLogin}>
                    Log in
                </Button>
                </form>
        
            </div>

        );
    }
}