import React from 'react'
//import axios from 'axios'

import '../styles/personList.css';

const API_URL = process.env.REACT_APP_API_URL

const personList = () => {
    

  console.log(API_URL)
  return (
    <div class="person-list">
      <h2>
        To edit  a person list</h2></div>
  )
}

export default personList;