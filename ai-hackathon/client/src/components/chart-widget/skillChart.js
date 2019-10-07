import React, { Fragment } from 'react'
import { BarChart, CartesianGrid, XAxis, YAxis, Label, LabelList, Bar, ReferenceLine, ResponsiveContainer } from 'recharts'

const skillChart = () => {

  const data = [
    {
      name: "Python",
      level: 0.25
    },
    {
      name: "HTML5",
      level: 0.5
    },
    {
      name: "R",
      level: 0.75
    },
    {
      name: "Java",
      level: 0.25
    },
    {
      name: "PHP7",
      level: 0.5
    }
  ]

  const sortData = data.sort((a,b) => (a.level < b.level) ? 1 : -1 )

  return (
    <Fragment>
      <h2 className="text-center">Skill Chart</h2>
      <ResponsiveContainer height={350} width="100%">
        <BarChart
          layout="vertical"
          data={sortData}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" />
          <YAxis dataKey="name" type="category" />
          <Bar dataKey="level" fill="#666666" />
        </BarChart>
      </ResponsiveContainer>
    </Fragment>
  )
}

export default skillChart
