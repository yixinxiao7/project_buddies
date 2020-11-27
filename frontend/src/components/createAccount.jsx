import React from 'react';


export default class CreateAccount extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        username: '',
        password: '',
        confirmPassword: '',
        hidden: true,
      };
      this.handleSubmit = this.handleSubmit.bind(this);
      this.toggleShow = this.toggleShow.bind(this);
    }


    handleSubmit(event) {
      event.preventDefault();
      
      if (this.state.password != this.state.confirmPassword) {
        alert("Passwords do not match!");
        return;
      }
      const {url} = this.props;
      const userPass = JSON.stringify({ username: this.state.username, password: this.state.password });
      fetch(url,  {
        method: 'POST',
        credentials: 'include',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: userPass })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {  // TODO, redirect user to account success page
          this.setState({
            username: '',
            password: '',
            confirmPassword: '',
          });
        });
    }

    toggleShow() {
      this.setState({ hidden: !this.state.hidden });
    }
  
    render() {
        const { username } = this.state;
        const { password } = this.state;
        const { confirmPassword } = this.state;
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
              <input
                  type={this.state.hidden ? 'password' : 'text'}
                  name="confirmPassword"
                  value={confirmPassword}
                  placeholder="Confirm password"
                  onChange={(e) => this.setState({ confirmPassword: e.target.value })}
              />
              <button onClick={this.toggleShow}>Show / Hide</button>
              <form onSubmit={this.handleSubmit}>
                <input
                    type="submit"
                    name="submitButton"
                    value="Create Account"
                />    
            </form>
          </div>
        );
    }
  }