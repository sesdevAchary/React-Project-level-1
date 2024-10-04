import React from 'react'

const API_URL= process.env.REACT_APP_API_URL


const personEdit=()=>{
    console.log(API_URL)

    return (
        <div>
            <h2>
                To edit  a person detail</h2></div>
    )
}

export default personEdit;