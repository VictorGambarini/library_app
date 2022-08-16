import React from 'react';
import './NavBar.css';
import logo from '../icon.ico';

export const NavBar = () => {
  return (
    <div className='nav-bar'>
        <ul className='nav-bar-list'>
            <li key="Logo">
                <img className='logo-img' src={logo}></img>
                <span className='logo-title'>Awesome Library</span>
            </li>
            <li key="Home">Home</li>
            <li key="Members">Members</li>
            <li key="Books">Books</li>
        </ul>
    </div>
  )
};
