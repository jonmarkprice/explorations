const React = require('react');

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.echo = this.echo.bind(this); // name of func
  }

  // We can access "this.textInput"
  echo() {
    // console.log(this.textInput); // dom node (?)
    console.log(this.textInput.value);
  }

  render() {
    return (
      <form className="dbg"
        onSubmit={event => {
          event.preventDefault();
          this.echo(); // bound to Form component
        }
      }> 
        <input type="text" id="rename"
         ref={input => { this.textInput = input; }}/>
        <input type="submit" value="Update" />
      </form>
    );
  }
}

module.exports = Form;
