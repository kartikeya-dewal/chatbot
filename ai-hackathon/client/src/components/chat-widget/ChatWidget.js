import React, { Fragment, useEffect } from 'react';
import { Widget, addResponseMessage } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';
import axios from 'axios';

const ChatWidget = () => {
  useEffect(() => {
    addResponseMessage('Hi! I am the interview chatbot Hirend');
  }, []);

  const handleNewUserMessage = newMessage => {
    // Fetch response from backend
    axios
      .put(
        '/api/user/1/',
        { userText: newMessage },
        {
          headers: { 'Content-Type': 'application/json' }
        }
      )
      .then(response => {
        console.log(response.data);
        addResponseMessage(response.data.message.toString());
      });
  };

  return (
    <Fragment>
      <Widget
        handleNewUserMessage={message => handleNewUserMessage(message)}
        title='Hirend'
        subtitle={`G'day`}
      />
    </Fragment>
  );
};

export default ChatWidget;
