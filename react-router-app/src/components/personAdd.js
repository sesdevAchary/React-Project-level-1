import React ,{useState}from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

import Notification from './notification.'
   

const API_URL = process.env.REACT_APP_API_URL;


const personAdd = ({ onPersonAdd =()=>{  }})=>{   {/* execute a no-op function.*/}
   const [ name,setName]= useState( ' ')
   const[ age,setAge] = useState(' ')
   const [showNotification, setShowNotification] = useState(null); {/* initialized to null, indicating no notification is shown initially*/}
   

   const handleSubmit= async(e)=>{
       e.preventDefault(); {/*  prevents the default form submission behavior, which typically refreshes the page*/}

       if(!name  || !age) return; {/* checks if name and age is falsy (undef,missing,null)*/}

       try{
        const response = await post(API_URL,{name,age});
        const newPersonId = response.data.id;{/* extracts the id of the newly added person from the response data.*/}
         
        setName('');
        setAge('');  {/* reset the name and age state variables to empty strings, clearing the form inputs.*/}
         


       // successfully person added notification shown //
        setShowNotification({type:'success',text:`person "${response.data.name}" added successfully`});
        setTimeout(() => navigate(`/person/${newPersonId}`), 2000); {/*Wait for 2 seconds before navigating*/}
       } catch(error){
          console.error('error adding person :',error);
          setShowNotification({type: 'error',text:'Failed to add a person.Try again'});
       }
   };
   const handleCloseNotification = () => {
    setShowNotification(null);
    };
 
    return(
     <div className = 'box-container'>
        <h2> ADD PERSON </h2>
        <form onSubmit={handleSubmit} className='form-container'>
            <input 
            type='text'
            placeholder='Name'
            value={name}
            onChange={(e)=> setName(e.target.value)}
            required
            className = 'input-field'
            />

            <input 
            type = 'number'
            placeholder='Age'
            value={age}
            onChange={(e)=>setAge(e.target.value)}
            required
            className='input-field'
            />
            <div className='button-group'>
                <button type="submit" className='btn btn-add'>ADD PERSON</button>
                <button type="button" className="btn btn-cancel" onClick={() => navigate('/')}>Cancel</button>

            </div>

            
        </form>

        {showNotification && <Notification message={showNotification} onClose={handleCloseNotification} />}

     </div>
);
};
export default personAdd;