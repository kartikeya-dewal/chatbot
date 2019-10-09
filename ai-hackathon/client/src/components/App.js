import React, { Fragment } from 'react';
import Header from './layout/Header';
import { Switch, Route, Link } from 'react-router-dom';
import ChatWidget from './chat-widget/ChatWidget';
import CandidateList from './page/CandidateList';
import Candidate from './page/Cadidate';

const App = () => {
  return (
    <Fragment>
      <Header />
      <div className='container'>
        <Switch>
          <Route
            path="/recruiter/user/:id"
          >
            <Candidate />
          </Route>
          <Route
            path="/recruiter"
          >
            <CandidateList />
          </Route>
          <Route
            exact
            path="/"
          >
            <div className='chat-widget'>
              <h1 className="text-center">Chat with me!!!</h1>
              <Link to="/recruiter">Admin Log-in</Link>
              <ChatWidget />
            </div>
          </Route>
        </Switch>
      </div>
    </Fragment>
  );
};

export default App;
