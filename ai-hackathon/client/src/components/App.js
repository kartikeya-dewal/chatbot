import React, { Fragment } from 'react';
import Header from './layout/Header';
import ChatWidget from './chat-widget/ChatWidget';
import EduChart from './chart-widget/eduChart';
import SentiChart from './chart-widget/sentiChart';
import SkillChart from './chart-widget/skillChart';
import ResChart from './chart-widget/resChart';

const App = () => {
  return (
    <Fragment>
      <Header />
      <div className='container'>
        <div className="row charts-wrapper">
          <div className="col-12 col-md-6">
            <EduChart />
          </div>
          <div className="col-12 col-md-6">
            <SentiChart />
          </div>
          <div className="col-12 col-md-6">
            <SkillChart />
          </div>
          <div className="col-12 col-md-6">
            <ResChart />
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
