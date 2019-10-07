import React, { Fragment } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer } from 'recharts'

const sentiChart = () => {
  const data = [
    {
      "sentiValue": 0.87
    },
    {
      "sentiValue": 0.8
    },
    {
      "sentiValue": -0.2
    },
    {
      "sentiValue": 0.38
    },
    {
      "sentiValue": 0.45
    }
  ]

  return (
    <Fragment>
      <h2 className="text-center">Sentimental Level</h2>
      <ResponsiveContainer height={350} width="100%">
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis hide />
          <YAxis domain={[-1, 1]} />
          <Line type="monotone" dataKey="sentiValue" />
        </LineChart>
      </ResponsiveContainer>
    </Fragment>
  )
}

export default sentiChart
