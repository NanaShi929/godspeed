import React from "react";
import axios from "axios";
export class DisplayData extends React.Component {
  constructor() {
    super();
    this.state = {
      dat: [],
    };
  }

  componentDidMount() {
    /*let dep = prompt('enter dept')*/
    axios.get("http://127.0.0.1:5000/fetchrecs"/*,
  { params: { dept: dep } }*/).then(res => { this.setState({ dat: res.data }) })
      .catch(err => console.log(err))
  }


  render() {
    var trs =
      this.state.dat.length == 0 ? (
        <h2>No data</h2>
      ) : (
        this.state.dat.map((e) => (
          <tr>

            <td>
              {e.rollno}

            </td>

            <td>
              {e.name}

            </td>

            <td>
              {e.sub}

            </td>

          </tr>
        ))
      );
    return (
      <table border="2.0">
        <th>Rollno</th>
        <th>Name</th>
        <th>Sub</th>

        <tbody>
          {trs}
        </tbody>

      </table>
    );
  }
}