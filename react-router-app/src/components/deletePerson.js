import React from 'react';

const deletePerson = ({ id, onDelete }) => {
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