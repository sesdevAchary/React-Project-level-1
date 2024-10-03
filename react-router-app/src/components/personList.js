import react from 'react'
import axios from 'axios'

const personList=()=>{
  const output = axios.get("https://5000-sesdevachar-reactprojec-vjtekaj7bdq.ws-us116.gitpod.io/persons")
  console.log(output);
  

  const API_URL= process.env.REACT_APP_API_URL
  console.log(API_URL)
    return (
        <div>
            <h2>
                To edit  a person list</h2></div>
    )
}

export default personList;