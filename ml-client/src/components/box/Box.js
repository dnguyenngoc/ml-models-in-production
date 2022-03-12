import React from 'react';
import {ArrowUpOutlined, ArrowDownOutlined} from '@ant-design/icons'


export default class Box extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name: this.props.name,
            value: this.props.value,
            currency: this.props.currency,
            icon: this.props.icon,
            increaseValue: this.props.increaseValue || 12,
            isIncrease: this.props.isIncrease
        }
       
    }
    render(){
        return(
            <div className='box'>
                <div className='box-avatar'>
                    { this.state.isIncrease ? <ArrowUpOutlined/> : <ArrowDownOutlined />}
                    <p className={this.state.isIncrease ? "" : "decrease"}>{this.state.increaseValue}%</p>
                    <img src={this.state.icon} alt={this.state.icon}></img>
                </div>
                <div className='box-value'>
                    {this.state.value}{this.state.currency}
                </div>
                <div className='box-title'>
                    {this.state.name}  
                </div>
               
               
            
            </div>
        );
    }
}
