import React from 'react'
import axios from 'axios'
import { DisplayData } from './Appdisp'
import { DeleteData } from './DeleteData';
import { UpdateData } from './UpdateData';
export class FormData extends React.Component {
    constructor() {
        super()
        this.state = {
            rollno: '',
            name: '',
            sub: ''
        }
    }

    submit = (e) => {
        e.preventDefault();
        var d = this.state
        axios.post("http://127.0.0.1:5000/insert", d)

    }
    change = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }

    render() {
        return (
            <div>


                <form onSubmit={this.submit}>
                    Rollno: <input type="text" name="rollno" onChange={this.change} /> <br></br>
                    Name: <input type="text" name="name" onChange={this.change} /><br></br>
                    Sub: <input type="text" name="sub" onChange={this.change} /><br></br>
                    <button>submit</button>
                </form>
                <DisplayData />
                <DeleteData />
                <UpdateData />
            </div>
        )
    }

}
