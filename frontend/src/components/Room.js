import React, { Component } from "react";

export default class Room extends Component {
  constructor(props) {
    super(props);
    this.state = {
      votes: 5,
      guest: false,
      isHost: false,
    };
    this.roomCode = this.props.match.params.roomCode;
  }
    getRoomDetails(){
        fetch("/api/get-info" + "?code=" + this.roomCode)
            .then((response) => response.json())
            .then((data) => {
                this.setState({
                    votes: data.votes,
                    guest: data.guest_pause,
                    isHost: data.host,
                });
            });
  }


  render() {
    return (
      <div>
        <h3>{this.roomCode}</h3>
        <p>Votes: {this.state.votes}</p>
        <p>Guest Can Pause: {this.state.guest.toString()}</p>
        <p>Host: {this.state.isHost.toString()}</p>
      </div>
    );
  }
}