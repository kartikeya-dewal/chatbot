import React from 'react';
import {Link} from 'react-router-dom';

const Header = () => {
  return (
    <nav className='navbar navbar-light bg-light'>
      <span className='navbar-brand mb-0 h1'><Link to="/">Chatbot</Link></span>
    </nav>
  );
};

export default Header;
