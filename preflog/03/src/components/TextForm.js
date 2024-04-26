import React, { useState } from 'react'
// console.log
export default function TextForm(props) {
    const [text, setText] = useState();
    const handleUpClick = () => {
        console.log("uppercase was clicked" + text);
        let newText = text.toUpperCase();
        setText(text.toUpperCase)
    }
    const handleOnChange = (event) => {
        console.log("uppercase was clicked");
        setText(event.target.value);
    }
    return (
        <div>
            <h1>{props.heading}</h1>
            <div className="form-floating">
                <textarea className="form-control" value={text} onChange={handleOnChange} id="mybox" placeholder='Enter'></textarea>
            </div>
            <button className="btn btn primary" onClick={handleUpClick}>convert to uppercase</button>
        </div>
    )
}
