import React from 'react';
import { Line } from 'react-chartjs-2';


export default class MultiAxisLine extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name: this.props.name,
            data: {
                labels: [
                '01/10', '02/10', '03/10', '04/10', '05/10', 
                '06/10', '07/10', '08/10', '09/10', '10/10',
                '11/10', '12/10', '13/10', '14/10', '15/10',
                '16/10', '17/10', '18/10', '19/10', '20/10',
                '21/10', '22/10', '23/10', '24/10', '25/10',
                '26/10', '27/10', '28/10', '29/10', '30/10',
               ],
                datasets: [
                  {
                    label: 'USD',
                    data: [
                      12, 19, 30, 50, 2000, 1730,1742, 494, 300, 750, 230, 30,12, 
                      19, 30, 35, 20, 3,45, 19, 30, 65, 112, 30,120, 
                      19, 43, 5, 42, 43,144, 19, 34, 54, 20, 30,
                    ],
                    fill: false,
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgba(255, 99, 132, 0.2)',
                    yAxisID: 'y-axis-1',
                  },
                  {
                    label: 'Number of people',
                    data: [ 12, 19, 30, 50, 534, 430,132, 619, 530, 150, 420, 30,12, 
                      19, 30, 35, 20, 993,999, 1229, 30, 65, 112, 30,120, 
                      19, 43, 5, 42, 43,144, 19, 34, 54, 20, 30,],
                    fill: false,
                    backgroundColor: 'rgb(54, 162, 235)',
                    borderColor: 'rgba(54, 162, 235, 0.2)',
                    yAxisID: 'y-axis-2',
                  },
                ],
            },
            options: {
                scales: {
                  yAxes: [
                    {
                      type: 'linear',
                      display: true,
                      position: 'left',
                      id: 'y-axis-1',
                    },
                    {
                      type: 'linear',
                      display: true,
                      position: 'right',
                      id: 'y-axis-2',
                      gridLines: {
                        drawOnArea: false,
                      },
                    },
                  ],
                },
            }
        }
    }
    render(){
        return (

            <div>
                <div className='header'>
                    <h1 className='title'>{this.state.name}</h1>
                </div>
                <Line data={this.state.data} options={this.state.options} />
            </div>
        );
    }
}

