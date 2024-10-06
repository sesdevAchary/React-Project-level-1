import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

import '../styles/PersonEdit.css'; // Component-specific styles

const API_URL = process.env.REACT_APP_API_URL;

const PersonEdit = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [person, setPerson] = useState({ name: '', age: '' });

  useEffect(() => {
    const fetchPerson = async () => {
      try {
        const response = await axios.get(`${API_URL}/${id}`);
        setPerson(response.data);
      } catch (error) {
        console.error('Error fetching person:', error);
      }
    };
    fetchPerson();
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setPerson({ ...person, [name]: value });
  };

  const handleUpdate = async (e) => {
    e.preventDefault();
    try {
      await axios.put(`${API_URL}/${id}`, person);
      navigate(`/person/${id}`); // Redirect to person details page after update
    } catch (error) {
      console.error('Error updating person:', error);
    }
  };

  const handleCancel = () => {
    navigate(`/person/${id}`); // Navigate back to the person details page
  };

  const handleHome = () => {
    navigate('/'); // Navigate back to the home page
  };
