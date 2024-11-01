import React ,{useEffect,useState} from 'react'
import {useParams,Link,useNavigate } from 'react-router-dom';
import axios from 'axios'; 
import Notification from './notification.js'


import '../styles/personList.css'

const API_URL = process.env.REACT_APP_API_URL


const personDetail=()=>{
  const{id}= useParams(); /* to extract id parameter */
  const navigate = useNavigate(); /* to programmatically navigate within the application */
  const [person,setPerson]= useState(null);
  const [ showNotification,setShowNotification]=useState(null);

}

export default personDetail;