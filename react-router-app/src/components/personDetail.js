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



  // to fetch data //

  useEffect(()=>{
    const fetchPerson = async()=>{
        try{
            console.log('fetching data from');
            const response = await axios.get(`${API_URL}/${id}`);
            console.log('person data:', response.data);
            setPerson(response.data);
        }catch (error){
            console.error('Error fetching person:', error.response || error.message);
            setShowNotification({ type: 'error', text: 'Error loading person details.' });
        }
    }

    fetchPerson();
  })
}

export default personDetail;