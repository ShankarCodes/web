import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import { Form, FormControl, Button } from 'react-bootstrap';
class Welcome extends React.Component
{
  render()
  {
  return <h1 >Hello {this.props.name}</h1>
  }
}
class Clock extends React.Component {
  constructor(props)
  {
    super(props);
    this.state= {date: new Date()}

  }
  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }
  componentWillUnmount() {
    clearInterval(this.timerID);
  }
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
  tick() {
    this.setState({
      date: new Date()
    });
  }

}
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text"  value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
        <Button variant="primary">Hello</Button>
      </form>
    );
  }
}
export { Welcome,Clock,NameForm}