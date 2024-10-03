// src/App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import PersonList from './components/personList';
import PersonDetail from './components/personDetail';
import PersonAdd from './components/personAdd';
import Notification from './components/notification';
import NotFound from './components/notFound';
import PersonEdit from './components/personEdit';
import './App.css'; // Global styles

const App = () => {
    return (
        <Router>
            <div className="box-container">
                <Routes>
                    <Route path="/" element={<PersonList />} />
                    <Route path="/add" element={<PersonAdd />} />
                    <Route path="/ntfcn" element={<Notification />} />
                    <Route path="/nofound" element={<NotFound/>} />


                    <Route path="/edit" element={<PersonEdit />} />
                    <Route path="/person" element={<PersonDetail />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;