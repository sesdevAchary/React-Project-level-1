import React from 'react';

const deletePerson = ({ id, onDelete }) => { {/* functional component with 2 props*/}
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this person?')) {
      onDelete(id);
    }
  };

  return (
    <button className="btn btn-delete" onClick={handleDelete}>
      Delete
    </button>
  );
};

export default deletePerson;



/* The DeletePerson component provides a button for deleting a person. When clicked,
 it prompts the user for confirmation and, if confirmed, 
 invokes a provided onDelete function with the person's id.*/