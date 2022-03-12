import React from 'react';
import { Bar } from 'react-chartjs-2';


export default class HorizontalBar extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name: this.props.name || 'HorizontalBar',
            data: {
                labels: ['Duy', 'Hung', 'Nghia', 'My', 'An', 'Vin','Huy',"T. Nghia", "Nhue", "Loz"],
                datasets: [
                  {
                    label: 'USD',
                    data: [12, 19, 3, 5, 2, 3, 7,8,9,6],
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
                ],
            },
            options: {
                indexAxis: 'y',
                elements: {
                  bar: {
                    borderWidth: 2,
                  },
                },
                responsive: true,
                plugins: {
                  legend: {
                    position: 'right',
                  },
                  title: {
                    display: false,
                  },
                },
            }
        }
    }
    render(){
        return(
            <div className='horizontal-bar'>
                <div className='header'>
                    <h1 className='title'>{this.state.name}</h1>
                </div>
                <Bar data={this.state.data} options={this.state.options}/>
            </div>
        );
    }
}
