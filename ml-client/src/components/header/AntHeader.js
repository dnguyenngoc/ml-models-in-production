import React from "react";

export default class AntHeader extends React.Component{
    constructor(props){
        super(props);
        this.state = {

        }
    }
    render(){
        return (
            <div className="ant-header-page">

                <header className="header-final">
                    <h5>Demo ML Models In Production</h5>
                </header>
            </div>
        )
    }
}