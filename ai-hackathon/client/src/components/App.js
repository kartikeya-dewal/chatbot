import React, { Fragment } from 'react';
import Header from './layout/Header';
import ChatWidget from './chat-widget/ChatWidget';
import EduChart from './chart-widget/eduChart';

const App = () => {
  return (
    <Fragment>
      <Header />
      <div className='container chat-widget'>
        <EduChart />
        <ChatWidget />
      </div>
    </Fragment>
  );
};

export default App;
