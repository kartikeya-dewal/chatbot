import React, { Fragment } from 'react';
import { Widget } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';

const ChatWidget = () => {
  const handleNewUserMessage = newMessage => {
    alert(`New message incoming: ${newMessage}`);
    // TODO: Send the message to the backend API
  };

  return (
    <Fragment>
      <Widget
        handleNewUserMessage={message => handleNewUserMessage(message)}
        title='Chatbot'
        subtitle={`G'day`}
      />
    </Fragment>
  );
};

export default ChatWidget;
