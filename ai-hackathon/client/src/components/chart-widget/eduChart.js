import React, { Fragment, useState } from 'react'
import { BarChart, CartesianGrid, XAxis, YAxis, Label, LabelList, Bar, ReferenceLine } from 'recharts'
const Chart = () => {
  const [width, setWidth] = useState(400)
  const [height, setHeight] = useState(400)
  const data = [
    {
      "name": "Bachelor of Science",
      "eduLevel": 1,
      "reqLevel": 2
    }
  ];
  const eduData = [
    'no primary',
    'secondary',
    'graduate',
    'post graduate',
    'doctorate'
  ]
  const currentReqLevel= () => {
    if (data[0].reqLevel == data[0].eduLevel) {
      return null;
    } else if(data[0].reqLevel) {  
      return eduData[data[0].reqLevel];
    } else {
      return 'missing education data';
    }
  }
  const currentEduLevel = () => {
    if (data[0].eduLevel) {
      return eduData[data[0].eduLevel];
    } else {
      return 'missing education data';
    }
  }
  return (
    <Fragment>
      <h2>Education Level</h2>
      <BarChart
        width={width}
        height={height}
        data={data}
        margin={{ top: 15, right: 30, left: 20, bottom: 5 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name">
        <Label value="Education" position="top"/>
        </XAxis>
        <YAxis hide domain={[0, 6]} />
        <Bar dataKey="eduLevel" fill="#8884d8">
          <LabelList content={currentEduLevel} position="top" />
        </Bar>
        <ReferenceLine y={data[0].reqLevel} label={currentReqLevel()} stroke="red" strokeDasharray="3 3" />
      </BarChart>
      <p>Degree Title: {data[0].name}</p>
    </Fragment>
  )
}

export default Chart
