import React, { Component } from 'react';
import logo from './logo.svg';
import './App.scss';

class App extends Component {
  constructor() {
    super();

    this.state = {
      teams: []
    }
  }

  queryApi = () => {
    fetch('/teams')
      .then(response => {
        return response.json()
      }).then(json => {
        json.sort((a, b) => {
          return b.score - a.score;
        });

        this.setState({ teams : json })
      });
  }

  componentDidMount = () => {
    this.interval = setInterval(this.queryApi, 5 * 1000);
  }

  componentWillUnmount = () => {
    clearInterval(this.interval);
  }

  render = () => {
    return (
      <div className="App">
        <h1>Grand Tech Tournament</h1>
        <div className="leaderboard">
          <div className="leaderboard__row leaderboard__row--bold">
            <div className="leaderboard__row__team">Team Name</div>
            <div className="leaderboard__row__score">Score</div>
            <div className="leaderboard__row__handicaps">Handicaps</div>
          </div>
          { this.state.teams.map(e => {
            return (
              <div className="leaderboard__row" key={ e.name + e.score }>
                <div className="leaderboard__row__team">{ e.name }</div>
                <div className="leaderboard__row__score">{ e.score }</div>
                <div className="leaderboard__row__handicaps">
                  { e.handicaps.map(handicap => {
                    return <p key="handicap">{ handicap }</p>;
                  }) }
                </div>
              </div>
            );
          }) }
        </div>
        <img src={logo} className="App-logo" alt="logo" />
      </div>
    );
  }
}

export default App;
