import React from 'react';
import { Avatar } from 'antd';
import { UserOutlined } from '@ant-design/icons';
import AccountService from '../../services/api/account.service'


export default class Account extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            avatar_url: null
        }
    }
    componentDidMount(){
        AccountService.getUserInfo(response =>{
            this.setState({avatar_url: response.data.avatar_url})
        },(err) => {
            alert(err);
        });
    }
    render(){
        return (
            <div className='avatar'>
                {this.state.avatar_url === null ? <Avatar size={50} icon={ <UserOutlined /> }/> :
                <img className='image' src={this.state.avatar_url} alt="avatar"></img>
                }
            </div>
        );
    }
}
