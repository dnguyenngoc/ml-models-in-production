import React from 'react';
import { Line } from 'react-chartjs-2';


export default class LineChart extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      data: {
        labels: ['01/10', '02/10', '03/10', '04/10', '05/10', 
                 '06/10', '07/10', '08/10', '09/10', '10/10',
                 '11/10', '12/10', '13/10', '14/10', '15/10',
                 '16/10', '17/10', '18/10', '19/10', '20/10',
                 '21/10', '22/10', '23/10', '24/10', '25/10',
                 '26/10', '27/10', '28/10', '29/10', '30/10',

                ],
        datasets: [
          {
            label: '# of USD',
            data: [12, 19, 3, 5, 2, 3,12, 19, 3, 5, 2, 3,12, 
              19, 3, 35, 2, 3,12, 19, 3, 65, 112, 3,12, 19, 43, 5, 42, 43,12, 19, 34, 54, 2, 3,],
            fill: false,
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgba(255, 99, 132, 0.2)',
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    }
  }
  render(){
    return(
      <div className='line-chart'>
      <div className='header'>
        <h1 className='title'>Line Chart</h1>
      </div>
      <Line data={this.state.data} options={this.state.options} />
      </div>
    )
  }
}
