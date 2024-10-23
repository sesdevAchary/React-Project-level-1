import React , { useEffect,useState} from 'react' // hooks that manage state and side effects in functional components.//
import axios from 'axios';
import './PersonList.css';


/* The endpoint for fetching, adding, updating, and deleting persons.*/
const API_URL = 'https://3001-sesdevachar-reactprojec-7guw5cetzf4.ws-us116.gitpod.io/persons';


/* Functional component -> way to create components in react */
const PersonList=()=>{

  const [persons, setPersons] = useState([]); // array that holds the list of persons fetched from the API//
  const [newPerson, setNewPerson] = useState({ name: '', age: '' }); // object to store data for a new person being added//
  const [editingPerson, setEditingPerson] = useState(null); // object that holds the person currently being edited//
  const [loading, setLoading] = useState(true); //boolean to indicate whether the data is still being fetched.//

  /* hook to perform side effects on react component like (fetching data(here persons from the api) 
  , manipulating a dom)*/
  useEffect(()=>{
    fetchPersons(); // for fetching a list of persons from an API or another source.//
  },[]); // empty array is the depedency array




  // READ operation........................................................................................

  const fetchPersons= async ()=>{
    try{
      const response= await axios.get(API_URL); // axios is  used to fetch data from the api , AWAIT , pauses the execution of the function until the promise returned by axios.get is resolved. //
      setPersons(response.data); //response.data typically contains the list of persons fetched//
      setLoading(false); //indicating that the data fetching process has completed.//           
    } catch(error){
      console.log("error fatching person",error);  // console.error(" "error fatching person",error )//
      alert('Failed to fetch persons. Please try again.')
      setLoading(false);  //indicating that the fetch attempt has finished, even if it was unsuccessful.//
    }
  };
 


  // CREATE operation..................................................

  const addPerson = async (e) => {
    e.preventDefault(); // to prevent the page from refreshing //
    try{
      const response = await axios.post(API_URL,newPerson); // passing newPerson as the request body//

      setPersons([...persons,response.data]);/* updates the persons state ,creates an array
                                              (including existing person + newly updated person)
                                              (...) is used to create a new array with the current persons and the new entry*/
       setNewPerson({name:'',age:''}); //resets the newPerson state back to its initial state (empty name and age), likely to clear the input fields in the form.
       alert("New persons added:${response.data.name}");
  } catch (error) {
    console.error('Error adding person:', error); // logs any error that occurs during the POST request to the console for debugging purposes//
    alert('Failed to add person. Please try again.');
  }
};
    
  

  // UPDATE operation
  const updatePerson = async(e)=>{
    e.preventDefault();
    try{

      //sends a request to update a specific person's data on the server and stores the server's response in the response variable.//
      const response = await axios.put(`${API_URL}/${editingPerson.id}`,editingPerson); /* constructs the URL using API_URL(e.g./api/persons) and the id of the editingPerson.
                                                                                         editingPerson (an object) is sent as the request body, which contains the updated information*/
       
      //updates the state of the persons array by replacing the person who was edited//                                                                                         
      setPersons(persons.map(person=> person.id === editingPerson.id ? response.data : person)); /* map method creates a new array based on the existing persons array(iterates through each perosn in the array).
                                                                                                  next the condition checks if the id of the current person in the loop matches the id of the editingPerson
                                                                                                   if true -> replaces the current person data with response.data , else keeps the original person
                                                                                                  now , result of map is a new array where the updated person replaces the old one, while all other persons remain unchanged.*/

      setEditingPerson(null); /* resets the editingPerson state to null, indicating that no person is currently being edited.*/
      

      alert(`Person updated: ${response.data.name}`); /*a template literal, which allows for embedded expressions. retrieves the name property from the response.data object.
                                                        This is the updated name of the person returned by the server. */


    } catch (error) {
      console.error('Error updating person:', error);
      alert('Failed to update person. Please try again.');
    }
  };

  // DELETE operation
 const deletePerson= async(id)=>{
  try{
    await axios.delete(`${API_URL}/${id}`); /*placeholder is replaced with the actual id value passed to the deletePerson function, 
                                            targeting the specific resource to be deleted.
                                             e.g.-> await axios.delete('https://api.example.com/persons/123');*/
    setPersons(persons.filter(person=> person.id !== id));
    alert(`Person with ID ${id} has been removed.`);

  }catch (error) {
    console.error('Error deleting person:', error);
    alert('Failed to delete person. Please try again.');
  }
};

  if (loading) {
    return <div className="loading">Loading...</div>;
  }



  // component's render output.To return  a JSX structure containing a <div> with an <h2> header.//
  // return (
  //   <div className="person-list">
  //     <h2>Person List</h2>
      
  //     {/* Add Person Form , for calling  the addPerson function upon submission.*/}
  //     <form onSubmit={addPerson} className="add-person-form">
  //       <input
  //         type="text"
  //         value={newPerson.name}
  //         onChange={(e) => setNewPerson({...newPerson, name: e.target.value})}
  //         placeholder="Name"
  //         required
  //       />
  //       <input
  //         type="number"
  //         value={newPerson.age}
  //         onChange={(e) => setNewPerson({...newPerson, age: e.target.value})}
  //         placeholder="Age"
  //         required
  //       />
  //       <button type="submit" className="btn btn-add">Add Person</button>
  //     </form>

  // The JSx content........//
  return(
    <div>person-list
      <h2>Person list</h2>
       {/*ADD PERSON FORM , fro calling the addPerson function*/}
       <form onSubmit={addPerson} className="add-person-form"> {/*This prop sets up an event handler that listens for the form's submit event.*/}

       </form>
  
      {/* Person List */}
      <ul className="person-items">
        {persons.map(person => (
          <li key={person.id} className="person-item">
            {editingPerson && editingPerson.id === person.id ? (
              <form onSubmit={updatePerson} className="edit-person-form">
                <input
                  type="text"
                  value={editingPerson.name}
                  onChange={(e) => setEditingPerson({...editingPerson, name: e.target.value})}
                  required
                />
                <input
                  type="number"
                  value={editingPerson.age}
                  onChange={(e) => setEditingPerson({...editingPerson, age: e.target.value})}
                  required
                />
                <button type="submit" className="btn btn-update">Update</button>
                <button type="button" className="btn btn-cancel" onClick={() => setEditingPerson(null)}>Cancel</button>
              </form>
            ) : (
              <>
                <span className="person-info">{person.name} (Age: {person.age})</span>
                <div className="person-actions">
                  <button className="btn btn-edit" onClick={() => setEditingPerson(person)}>Edit</button>
                  <button className="btn btn-delete" onClick={() => deletePerson(person.id)}>Delete</button>
                </div>
              </>
            )}
          </li>
        ))}
      </ul>
      
    </div>
  );
};

export default PersonList;