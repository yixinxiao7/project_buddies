import React from 'react';


export default class Landing extends React.Component {
    constructor(props) {
      super(props);
      this.state = {};
    }
  
    render() {
        return (
            <div>
                <h1>Welcome to the most aesthetic website!!!!!</h1>
                <p>
                    <a href="/#/createAccount">Create Account</a>
                </p>
                <p>
                    <a href="/#/login">Login</a>
                </p>
                <p>
                    <a href="https://www.youtube.com/watch?v=qYWl5ou6R4g">i dare you to click me</a>
                </p>
            </div>
        );
    }
  }