import React, { Fragment } from "react";
import { ResponsiveContainer, PieChart, Pie, Cell, Sector} from "recharts";
const resChart = () => {
  const data = [
    {
      "name": "example1",
      "value": 0.8
    },
    {
      "name": "example2",
      "value": 0.2
    }
  ];

  const COLORS = ["#0088FE", "#FFF", "#FFBB28", "#FF8042"];
  return (
    <Fragment>
      <h2 className="text-center">Research Chart</h2>
      <ResponsiveContainer height={350} width="100%">
        <PieChart>
        <Pie
          data={data}
          dataKey="value"
          nameKey="name"
          startAngle={-180}
          endAngle={180}
          label
        >
          {
            data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
          }
        </Pie>
      </PieChart>
      </ResponsiveContainer>
    </Fragment>
  );
};

export default resChart;
