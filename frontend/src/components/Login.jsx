import React from 'react';
import { Redirect } from "react-router-dom";


export default class Login extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        username: '',
        password: '',
        redirect: false,
        hidden: true,
      };
      this.handleSubmit = this.handleSubmit.bind(this);
      this.toggleShow = this.toggleShow.bind(this);
    }


    handleSubmit(event) {
      event.preventDefault();
      const {url} = this.props;
      const userPass = JSON.stringify({ username: this.state.username, password: this.state.password});
      fetch(url,  {
        method: 'POST',
        credentials: 'include',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: userPass })
        .then((response) => {
          if (!response.ok) {
            response.text().then(error => {
              const json_error = JSON.parse(error);
              alert(json_error.error);
            })
          }
          return response.json();
        })
        .then((data) => {  // TODO, redirect user to account success page
          this.setState({
            redirect: true
          });
        });
    }

    toggleShow() {
      this.setState({ hidden: !this.state.hidden });
    }
  
    render() {
        const { username } = this.state;
        const { password } = this.state;
        const { redirect } = this.state;

        if (redirect) {
          return <Redirect to="/home" />
        }
        return (
            <div>
              <input
                  type="text"
                  name="username"
                  value={username}
                  placeholder="Username"
                  onChange={(e) => this.setState({ username: e.target.value })}
              />
              <input
                  type={this.state.hidden ? 'password' : 'text'}
                  name="password"
                  value={password}
                  placeholder="Password"
                  onChange={(e) => this.setState({ password: e.target.value })}
              />
              <button onClick={this.toggleShow}>Show / Hide</button>
              <form onSubmit={this.handleSubmit}>
                <input
                    type="submit"
                    name="submitButton"
                    value="Login"
                />
              </form>
            </div>
        );
    }
  }