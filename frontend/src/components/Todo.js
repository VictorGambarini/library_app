import React from 'react';
import axios from 'axios';

function TodoItem(props) {
    const deleteTodoHandler = () => {
        const url = 'http://127.0.0.1:8000/members/delete/'+props.todo.id
        axios.delete(url)
        .then(res => console.log(props.todo.id))
    }
    return(
        <div>
            <p>
                <span>{props.todo.id}</span>
                <span>{props.todo.name}</span>
                <button onClick={() => deleteTodoHandler(props.todo.id)}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default TodoItem;