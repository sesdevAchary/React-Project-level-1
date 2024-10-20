import React , { useEffect,useState} from 'react' // hooks that manage state and side effects in functional components.//
import axios from 'axios';
import './PersonList.css';


/* The endpoint for fetching, adding, updating, and deleting persons.*/
const API_URL = 'https://3001-sesdevachar-reactprojec-7guw5cetzf4.ws-us116.gitpod.io/persons';


/* Functional component -> way to create components in react */
const PersonList=()=>{

  const [persons, setPersons] = useState([]); // array that holds the list of persons fetched from the API//
  const [newPerson, setNewPerson] = useState({ name: '', age: '' }); // bject to store data for a new person being added//
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
    e.preventDefault();
    try {
      const response = await axios.post(API_URL, newPerson); 
      setPersons([...persons, response.data]);
      setNewPerson({ name: '', age: '' });
      alert(`New person added: ${response.data.name}`);
    } catch (error) {
      console.error('Error adding person:', error);
      alert('Failed to add person. Please try again.');
    }
  };

  // UPDATE operation
  const updatePerson = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(`${API_URL}/${editingPerson.id}`, editingPerson);
      setPersons(persons.map(person => person.id === editingPerson.id ? response.data : person));
      setEditingPerson(null);
      alert(`Person updated: ${response.data.name}`);
    } catch (error) {
      console.error('Error updating person:', error);
      alert('Failed to update person. Please try again.');
    }
  };

  // DELETE operation
  const deletePerson = async (id) => {
    try {
      await axios.delete(`${API_URL}/${id}`);
      setPersons(persons.filter(person => person.id !== id));
      alert(`Person with ID ${id} has been removed.`);
    } catch (error) {
      console.error('Error deleting person:', error);
      alert('Failed to delete person. Please try again.');
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="person-list">
      <h2>Person List</h2>
      
      {/* Add Person Form */}
      <form onSubmit={addPerson} className="add-person-form">
        <input
          type="text"
          value={newPerson.name}
          onChange={(e) => setNewPerson({...newPerson, name: e.target.value})}
          placeholder="Name"
          required
        />
        <input
          type="number"
          value={newPerson.age}
          onChange={(e) => setNewPerson({...newPerson, age: e.target.value})}
          placeholder="Age"
          required
        />
        <button type="submit" className="btn btn-add">Add Person</button>
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