import React from 'react';
import 'antd/dist/antd.css';
import { Spin, Space } from 'antd';

export default class SpinLoading extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      size: props.size || ""
    }
  }
  render(){
    return(
      <Space size="middle">
        <Spin size={this.state.size}/>
      </Space>
    )
  }
}


