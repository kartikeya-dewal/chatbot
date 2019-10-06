import React, { Fragment } from 'react';
import Header from './layout/Header';
import ChatWidget from './chat-widget/ChatWidget';
import EduChart from './chart-widget/eduChart';

const App = () => {
  return (
    <Fragment>
      <Header />
      <div className='container'>
        <div className="row">
          <div className="col-12 col-md-6">
            <EduChart />
          </div>
        </div>
        <div className='chat-widget'>
          <ChatWidget />
        </div>
      </div>
    </Fragment>
  );
};

export default App;
