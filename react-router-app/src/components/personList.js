import React, { useEffect, useState } from 'react'
import {Link} from "react-router-dom"
import axios from 'axios'

import Notification from './notification'
import '../styles/personList.css';

const API_URL = process.env.REACT_APP_API_URL
console.log(API_URL)


const personList = () => {
    const[people,setPeople]=useState([]);/*people-> to hold an array of person of object 
                                            useState-> Initializes people with an empty array,
                                            the component will eventually populate this array with data,from an API or other data source.*/

    const[notification,setNotification]=useState("");

    useEffect(()=>{   /* useEffect hook allows to perform side effects in a functional component*/
      const fetchPeople=async()=>{
        try{
          const response = await axios.get(API_URL)
          console.log(response)
          setPeople(response.data);
        }catch(error){
          console.error('error fetching',error)
        }
      };
      fetchPeople(); /* initiating the API request.*/

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