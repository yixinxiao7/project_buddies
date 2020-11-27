import React, { Component } from "react";
import { render } from "react-dom";
import { HashRouter, Route, Switch, Redirect } from "react-router-dom";
import Home from './components/home.jsx';
import CreateAccount from './components/createAccount.jsx';
import Login from './components/Login.jsx';

class App extends Component {
  render() {
    return (
      <HashRouter>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/createAccount" component={() => <CreateAccount url={`api/credentials/`}/>} />
          <Route path="/login" component={() => <Login url={`api/sessions/`}/>} />
          {/* <Route exact path="/404" component = {NotFound}/> */}
          {/* <Redirect to="/404"/> */}
        </Switch>
      </HashRouter>
    );
  }
}

const container = document.getElementById("app");
render(<App />, container);