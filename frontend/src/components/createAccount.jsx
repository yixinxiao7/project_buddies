import React from 'react';


export default class CreateAccount extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        username: '',
        password: '',
      };
      this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleSubmit(event) {
      event.preventDefault();
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
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {  // TODO, redirect user to account success page
          this.setState({
            username: '',
            password: '',
          });
        });
    }
  
    render() {
        const { username } = this.state;
        const { password } = this.state;
        return (
            <div>
            <form onSubmit={this.handleSubmit}>
                <input
                    type="text"
                    name="username"
                    value={username}
                    placeholder="Username"
                    onChange={(e) => this.setState({ username: e.target.value })}
                />
                <input
                    type="text"
                    name="password"
                    value={password}
                    placeholder="Password"
                    onChange={(e) => this.setState({ password: e.target.value })}
                />
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