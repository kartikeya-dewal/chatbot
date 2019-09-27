import React, { Fragment } from 'react';
import Header from './layout/Header';
import ChatWidget from './chat-widget/ChatWidget';

const App = () => {
  return (
    <Fragment>
      <Header />
      <div className='container chat-widget'>
        <ChatWidget />
      </div>
    </Fragment>
  );
};

export default App;
