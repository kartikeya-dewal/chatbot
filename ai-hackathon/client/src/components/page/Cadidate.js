import React, { Fragment, useState, useEffect } from "react";
import EduChart from "../chart-widget/eduChart";
import SentiChart from "../chart-widget/sentiChart";
import SkillChart from "../chart-widget/skillChart";
import ResChart from "../chart-widget/resChart";
import { useParams } from "react-router-dom";
import axios from 'axios';

const Candidate = () => {
  const id = useParams();
  console.log(id);

  const [user, setUser] = useState([]);
 
  useEffect(() => {
    const result = axios
      .get(`/api/user/` + id.id )
      .then(result => {
        setTimeout(() => {
          console.log(result.data.data);
          setUser(result.data.data);
        }, 1000);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  return (
    <Fragment>
      <h3 className="text-center">Candidate: {user.name}</h3>
      <h4 className="text-center">Overall Score: {user.overall_score}</h4>
      <div className="row charts-wrapper">
        <div className="col-12 col-md-6">
          <EduChart id={id} />
        </div>
        <div className="col-12 col-md-6">
          <SentiChart id={id} />
        </div>
        <div className="col-12 col-md-6">
          <SkillChart id={id}/>
        </div>
        <div className="col-12 col-md-6">
          <ResChart id={id} />
        </div>
      </div>
    </Fragment>
  );
};

export default Candidate;
