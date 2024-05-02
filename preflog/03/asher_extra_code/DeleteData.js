import React from 'react';
import axios from 'axios';

export class DeleteData extends React.Component {
    constructor() {
        super();
        this.state = {
            rollno: ''
        };
    }

    submit = (e) => {
        e.preventDefault();
        axios.delete("http://127.0.0.1:5000/delete", { data: { rollno: this.state.rollno } })
            .then(res => console.log(res.data))
            .catch(err => console.log(err));
    }

    change = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    render() {
        return (
            <form onSubmit={this.submit}>
                Rollno: <input type="text" name="rollno" onChange={this.change} />
                <button>Delete</button>
            </form>
        );
    }
}