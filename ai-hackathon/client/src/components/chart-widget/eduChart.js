import React, { Fragment, useState, useEffect } from 'react';
import { BarChart, CartesianGrid, XAxis, YAxis, Label, LabelList, Bar, ReferenceLine, ResponsiveContainer } from 'recharts';
import { useParams } from "react-router-dom";
import axios from 'axios';

const Chart = (props) => {
  const [height, setHeight] = useState(400)
  const [width, setWidth] = useState(400)
  const id = useParams();
  const [edu, setEdu] = useState(false)

  useEffect(() => {
    const result = axios
      .get(`/api/user/` + id.id )
      .then(result => {
        setTimeout(() => {
          console.log(result.data.data.education_level)
          setEdu(result.data.data.education_level);
        }, 1000);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  // console.log(edu);

  // const data = [
  //   {
  //     "type": "Education",
  //     "name": "Bachelor of Life Science",
  //     "eduLevel": 1,
  //     "reqLevel": 3
  //   }
  // ];

  // Array of Education level description
  const eduData = [
    'no beginner',
    'graduate',
    'post graduate',
    'doctorate'
  ]

  // Return matching index with data to retrieve required level text
  const currentReqLevel = () => {
    if (edu.reqLevel == edu.eduLevel) {
      return null;
    } else if (edu.reqLevel) {
      return eduData[edu.reqLevel];
    } else {
      return 'missing education data';
    }
  }

  // Return matching index with data to retrieve education level text
  const currentEduLevel = () => {
    if (edu.eduLevel) {
      return eduData[edu.eduLevel];
    } else {
      return 'missing education data';
    }
  }
  if (!edu)
  return (
    <Fragment>
      <div class="alert alert-info" role="alert">
        Currently there is no data to display.
      </div>
    </Fragment>
  );
  
  return (
    <Fragment>
      <h2 className='text-center'>Education Level</h2>
      <ResponsiveContainer height={350} width="100%">
        <BarChart
          width={width}
          height={height}
          data={[edu]}
          margin={{ top: 15, right: 30, left: 20, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="type">
            <Label value="Education" position="top" />
          </XAxis>
          <YAxis hide domain={[0, 6]} />
          <Bar dataKey="eduLevel" fill="#8884d8">
            <LabelList content={currentEduLevel} position="top" />
          </Bar>
          <ReferenceLine y={edu.reqLevel} label={currentReqLevel()} stroke="red" strokeDasharray="3 3" />
        </BarChart>
      </ResponsiveContainer>
      <p className='text-center'>Degree Title: {edu.name}</p>
    </Fragment>
  )
}

export default Chart
