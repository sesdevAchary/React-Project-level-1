import React ,{useEffect,usestate} from 'react'
import {Link} from 'react-router-dom';
import axios from 'axios'; 

import Notification from './notification.js'
const API_URL = process.env.REACT_APP_API_URL


const personDetail=()=>{
    console.log(API_URL)

    return (
        <div>
            <h2>
                TO add details about person </h2></div>
    )
}

export default personDetail;