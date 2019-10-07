import React, { Fragment, useState } from 'react'
import { BarChart, CartesianGrid, XAxis, YAxis, Label, LabelList, Bar, ReferenceLine, ResponsiveContainer } from 'recharts'
const Chart = () => {
  const [height, setHeight] = useState(400)
  const [width, setWidth] = useState(400)
  const data = [
    {
      "type": "Education",
      "name": "Bachelor of Life Science",
      "eduLevel": 3,
      "reqLevel": 3
    }
  ];

  // Array of Education level description
  const eduData = [
    'no primary',
    'secondary',
    'graduate',
    'post graduate',
    'doctorate'
  ]

  // Return matching index with data to retrieve required level text
  const currentReqLevel = () => {
    if (data[0].reqLevel == data[0].eduLevel) {
      return null;
    } else if (data[0].reqLevel) {
      return eduData[data[0].reqLevel];
    } else {
      return 'missing education data';
    }
  }

  // Return matching index with data to retrieve education level text
  const currentEduLevel = () => {
    if (data[0].eduLevel) {
      return eduData[data[0].eduLevel];
    } else {
      return 'missing education data';
    }
  }

  return (
    <Fragment>
      <h2 className='text-center'>Education Level</h2>
      <ResponsiveContainer height={350} width="100%">
        <BarChart
          width={width}
          height={height}
          data={data}
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
          <ReferenceLine y={data[0].reqLevel} label={currentReqLevel()} stroke="red" strokeDasharray="3 3" />
        </BarChart>
      </ResponsiveContainer>
      <p className='text-center'>Degree Title: {data[0].name}</p>
    </Fragment>
  )
}

export default Chart
