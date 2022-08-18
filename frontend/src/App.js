import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import { NavBar } from './components/NavBar';
import { Routes, Route} from "react-router-dom";
import { Home } from './components/Home';
import { Members } from './components/Members';
import { Books } from './components/Books';

function App() {

  return (
    <div className="App list-group-item justify-content-center mx-auto" id="App">
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/members" element={<Members />} />
        <Route path="/books" element={<Books />} />
      </Routes>
    </div>
  );
}

export default App;
