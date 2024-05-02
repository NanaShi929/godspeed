import React from 'react';
import axios from 'axios';

export class UpdateData extends React.Component {
    constructor() {
        super();
        this.state = {
            rollno: '',
            name: '',
            sub: ''
        };
    }

    submit = (e) => {
        e.preventDefault();
        axios.put("http://127.0.0.1:5000/update", this.state)
            .then(res => console.log(res.data))
            .catch(err => console.log(err));
    }

    change = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    render() {
        return (
            <form onSubmit={this.submit}>
                Rollno: <input type="text" name="rollno" onChange={this.change} /><br/>
                Name: <input type="text" name="name" onChange={this.change} /><br/>
                Sub: <input type="text" name="sub" onChange={this.change} /><br/>
                <button>Update</button>
            </form>
        );
    }
}
