import React from 'react';
import './NavBar.css';
import logo from '../icon.ico';
import {Link} from 'react-router-dom';

export const NavBar = () => {
  return (
    <nav className='nav-bar'>
        <Link to="/">
          <img className='logo-img' src={logo}></img>
          <span className='logo-title'>Awesome Library</span>
        </Link>
      <ul>
        <Link to="/">
          <li key="Home">Home</li>
        </Link>
        <Link to="/members">
          <li key="Members">Members</li>
        </Link>
        <Link to="/books">
          <li key="Books">Books</li>
        </Link>
      </ul>
    </nav>
  )
};
