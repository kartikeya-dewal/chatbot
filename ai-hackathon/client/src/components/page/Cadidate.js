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
          console.log(result.data);
          setUser(result.data);
        }, 1000);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  return (
    <Fragment>
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
    </Fragment>
  );
};

export default Candidate;
