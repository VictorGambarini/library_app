import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import TodoView from './TodoListView';
import {LeftMenu} from "./LeftMenu"

export const Members = () => {
    const [todoList, setTodoList] = useState([{}])
    const [title, setTitle] = useState('')
    const [desc, setDesc] = useState('')
  
    // Read all todos
    function readAllTodos() {
      axios.get("http://127.0.0.1:8000/members/list/")
      .then(res => {
          setTodoList(res.data)
      })
    };
  
    // Post a todo
    const addTodoHandler = () => {
    axios.post("http://127.0.0.1:8000/members/create", {"name": title, "email": desc})
    .then(res => console.log(res))
    readAllTodos()
    }
  
    return (
        <div className='main-div'>
            <div className='left-side'>
                <LeftMenu />
            </div>
            <div className='righ-side'>
                <h1 className='card text-white bg-primary mb-1'>Task Manager</h1>
                <h6 className='card text-white bg-primary mb-3'>FASTAPI - React - MongoDB</h6>
                <div className='card-body'>
                    <h5 className='card text-white bg-dark mb-3'>Add Your Task</h5>
                    <span className='card-text'>
                    <input className='mb-2 form-control titleIn' onChange={event => setTitle(event.target.value)} placeholder='Title' />
                    <input className='mb-2 form-control desIn' onChange={event => setDesc(event.target.value)} placeholder='Description' />
                    <button className='btn btn-outline-primary mx-2 mb-2' id="addTaskBtn" onClick={addTodoHandler} >Add Task</button>
                    </span>
                    <h5 className='card text-white bg-dark mb-3'>Your Tasks</h5>
                    <div>
                    <TodoView todoList={todoList} />
                    </div>
                </div>
                <h6 className='card text-dark bg-warning py-1 mb-0'>Copyright 2022, All righs reserverd &copy;</h6>
            </div>
        </div> 
    )
  }
