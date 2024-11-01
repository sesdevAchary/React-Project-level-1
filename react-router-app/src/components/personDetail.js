import React ,{useEffect,usestate} from 'react'
import {useParams,Link,useNavigate } from 'react-router-dom';
import axios from 'axios'; 
import Notification from './notification.js'


import '../styles/personList.css'

const API_URL = process.env.REACT_APP_API_URL


const personDetail=()=>{
  const{id}= useParams(); /* to extract id parameter */
}

export default personDetail;