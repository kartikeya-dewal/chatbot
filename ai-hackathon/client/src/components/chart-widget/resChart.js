import React, {Fragment} from 'react'
import {ResponsiveContainer, PieChart, Pie, } from 'recharts'
const resChart = () => {
  const data = [
    {
      name: 'example1',
      value: 200
    },
    {
      name: 'example2',
      value: 400
    }
  ]
  return (
    <Fragment>
      <h2 className="text-center">Research Chart</h2>
      <ResponsiveContainer height={350} width="100%">
        <PieChart>
          <Pie isAnimationActive={false} data={data} outerRadius={100} fill="#8884d8" label />
        </PieChart>
      </ResponsiveContainer>
    </Fragment>
  )
}

export default resChart
