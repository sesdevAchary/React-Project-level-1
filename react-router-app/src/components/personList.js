import React, { useEffect, useState } from 'react'
import {Link} from "react-router-dom"
import axios from 'axios'

import notification from './notification'
import '../styles/personList.css';

const API_URL = process.env.REACT_APP_API_URL
console.log(API_URL)


const personList = () => {
    const[people,setPeople]=useState([]);
    const[notification,setNotification]=useState("");

    useEffect(()=>{
      const fetchPeople=async()=>{
        try{
          const response = await axios.get(API_URL)
          console.log(response)
          setPeople(response.data);
        }catch(error){
          console.error('error fetching',error)
        }
      };
      fetchPeople();

    },[]);


  return (
    <div class="person-list">
      <h2>
        To edit  a person list</h2>
        <Link to='/add' className="btn btn-add add-person-button"> ADD PERSON</Link>
        <table>
          <thead>
            <tr>
              <th>name</th>
              <th>Age</th>
            </tr>
          </thead>
       <tbody>
        {people.map(person=>(
          <tr key={person.id}>
            <td>
              <Link to={`/person/${person.id}`} className='person-name'>
              {person.name}</Link>
            </td>
            <td>perosn.age</td>
          </tr>
        ))}
       </tbody>
</table>
{notification && (
  <notification messsage={Notification} onclose ={() => setNotification('')} />
)}
        
        </div>
  );
};

export default personList;