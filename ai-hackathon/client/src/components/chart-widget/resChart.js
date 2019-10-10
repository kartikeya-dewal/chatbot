import React, {Fragment} from 'react'
import {ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
const resChart = () => {
  const data = [
    {
      name: 'example1',
      value: 0.8
    },
    {
      name: 'example2',
      value: 0.2
    }
  ]

  const COLORS = ['#0088FE', '#FFF', '#FFBB28', '#FF8042'];

  return (
    <Fragment>
      <h2 className="text-center">Research Chart</h2>
      <ResponsiveContainer height={350} width="100%">
        <PieChart>
          <Pie 
          data={data} 
          outerRadius={100} 
          fill="#8884d8" 
          label 
          dataKey={data.name}
          startAngle={-180}
          endAngle={180} >
            {
              data.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)
            }
          </Pie>
        </PieChart>
      </ResponsiveContainer>
    </Fragment>
  )
}

export default resChart
