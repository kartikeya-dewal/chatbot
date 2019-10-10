import React, { Fragment, useState, useEffect } from 'react'
import { BarChart, CartesianGrid, XAxis, YAxis, Label, LabelList, Bar, ReferenceLine, ResponsiveContainer } from 'recharts'
import { useParams } from "react-router-dom";
import axios from 'axios';

const skillChart = () => {
  const id = useParams()
  const [skill, setSkill] = useState(false)

  useEffect(() => {
    const result = axios
      .get(`/api/user/` + id.id )
      .then(result => {
        setTimeout(() => {
          console.log(result.data.data.skill_set);
          setSkill(result.data.data.skill_set);
        }, 1000);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  // const data = [
  //   {
  //     name: "Python",
  //     level: 0.25
  //   },
  //   {
  //     name: "HTML5",
  //     level: 0.5
  //   },
  //   {
  //     name: "R",
  //     level: 0.75
  //   },
  //   {
  //     name: "Java",
  //     level: 0.25
  //   },
  //   {
  //     name: "PHP7",
  //     level: 0.5
  //   }
  // ]

  // const sortData = data.sort((a,b) => (a.level < b.level) ? 1 : -1 )
  if (!skill)
  return (
    <Fragment>
      <div class="alert alert-info" role="alert">
        Currently there is no data to display.
      </div>
    </Fragment>
  );
  
  return (
    <Fragment>
      <h2 className="text-center">Skill Chart</h2>
      <ResponsiveContainer height={350} width="80%">
        <BarChart
          layout="vertical"
          data={skill}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" domain={[0,1]} tick={{fontSize: 12}} />
          <YAxis dataKey="name" type="category" tick={{fontSize: 12}}/>
          <Bar dataKey="level" label={{ fill: 'red', fontSize: 15 }} />
        </BarChart>
      </ResponsiveContainer>
    </Fragment>
  )
}

export default skillChart
