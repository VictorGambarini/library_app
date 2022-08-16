import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import { NavBar } from './components/NavBar';
import { TaskManager } from './components/TaskManager';

function App() {

  return (
    <div className="App list-group-item justify-content-center mx-auto" id="App">
      <NavBar />
      <TaskManager />
      
    </div>
  );
}

export default App;
