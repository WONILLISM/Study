import React from "react";
import PropTypes from "prop-types";

class App extends React.Component {
  state = {
    isLoading: true,
  };
  componentDidMount() {
    setTimeout(() => this.setState({ isLoading: false }), 6000);
  }
  render() {
    const { isLoading } = this.state; // ES6에서만 작동
    // return <div>{this.state.isLoading ? "Loading..." : "We are ready"}</div>; ES6 이하 작동
    return <div>{isLoading ? "Loading..." : "We are ready"}</div>;
  }
}

export default App;
