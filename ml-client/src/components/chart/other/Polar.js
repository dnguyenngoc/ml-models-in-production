import React from 'react';
import { PolarArea } from 'react-chartjs-2';

export default class Polar extends React.Component {
  constructor(props){
    super(props);
    this.state = {
        data: {
          labels: ['Geshin Impart', 'Tic Tac Ton', 'Minercraft', 'The Witcher',  'Don\'t Starve', 'React Chess'],
          datasets: [
            {
              label: '# of USD',
              data: [12, 33, 14, 21, 24, 32],
              backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)',
              ],
              borderWidth: 1,
            },
          ],
        },
        name: props.name || "Highest Grossing Game"
    }
  }
  render(){
    return(
      <div className='polar'>
        <div className='header'>
          <h1 className='title'>{this.state.name}</h1>
          <div className='links'>
          </div>
        </div>
        <PolarArea data={this.state.data} />
      </div>
    );
  }
}
