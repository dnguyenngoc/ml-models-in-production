import React from 'react';
import AntHeader from '../components/header/AntHeader';
import Footer from '../components/footer/Footer';



export default class DashBoard extends React.Component{
    constructor(props){
        super(props);
        this.state = {

        }
    }
    componentDidMount(){
      
    }
    onChange(date, dateString) {
        console.log(date, dateString);
    }
    render(){
        return (
            <div className='dashboard'>
                <AntHeader/>
               <div className='col-one'>
                    <div className='item'>
                        <div className='item-box'>
                            <h1 className='title'>Select Image</h1>
                            <div className='image'>Here</div>
                        </div>
                    </div>
                    <div className='item'>
                        <div className='item-box'>
                            <h1 className='title'>Result Image</h1>
                            <div className='image'>Here</div>
                        </div>
                    </div>
               </div>
               <Footer/>
            </div>
        );
    }
}
