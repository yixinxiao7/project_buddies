import React from 'react';


export default class AccountCreated extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
      };
    }

    render() {
        return (
            <div>
              <p>
                  Account Created Sucessfully!
              </p>
              <p>
                  <a href="/#"> Return to home. </a>
              </p>
            </div>
        );
    }
  }