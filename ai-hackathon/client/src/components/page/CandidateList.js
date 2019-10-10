import React, { Fragment, useState, useEffect } from "react";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import axios from "axios";

const CandidateList = () => {
  const [users, setUsers] = useState({ list: [] });

  const makeList = [];

  useEffect(() => {
    const result = axios.get("/api/user").then(result => {
      setTimeout(() => {
        console.log(result.data);
        setUsers({list: result.data})
      }, 1000);
    })
    .catch((error)=>{
      console.log(error);
    });
  }, []);

  const userList = [
    {
      id: 1,
      name: "John Doe",
      overallScore: 100
    },
    {
      id: 2,
      name: "Mary Jane",
      overallScore: 79
    },
    {
      id: 3,
      name: "Kat Heart",
      overallScore: 72
    },
    {
      id: 4,
      name: "Patrick Hendrick",
      overallScore: 45
    },
    {
      id: 5,
      name: "Ben McLoren",
      overallScore: 62
    }
  ];

  return (
    <Fragment>
      <div className="display1">User List</div>
      <ul>
        {userList.map((user, index) => {
          return (
            <li key={index}>
              Score: {user.overallScore}{" "}
              <Link to={`recruiter/user/${user.id}`}>{user.name}</Link>
            </li>
          );
        })}
      </ul>
    </Fragment>
  );
};

export default CandidateList;
