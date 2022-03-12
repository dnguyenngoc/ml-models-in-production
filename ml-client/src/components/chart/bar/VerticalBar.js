import React from 'react';
import { Bar } from 'react-chartjs-2';


export default class VerticalBar extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name: props.name || "Most Paid Users",
            data: {
                labels: ['Duy Nguyen', 'Hung Le', 'My Le', 'An Dang', 'Huy Hoang', 'Vin Tran', 'Heo', 'Ha', 'Leu Leu', 'Con Céc'],
                datasets: [
                    {
                        label: 'Minute',
                        data: [120, 190, 30, 70, 46, 43,111,111,111,111],
                        backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        ],
                        borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        ],
                        borderWidth: 1,
                  },
                ]
            },
            options: {
                scales: {
                  yAxes: [
                    {
                      ticks: {
                        beginAtZero: true,
                      },
                    },
                  ],
                },
            }
              
        }
    }
    render(){
        return (
            <div className='vertical-bar'>
                 <div className='header'>
                  <h1 className='title'>{this.state.name}</h1>
                </div>
                <Bar data={this.state.data} options={this.state.options} />
            </div> 
        );
    }
}



