import React, { Fragment, useState, useEffect } from "react";
import { ResponsiveContainer, PieChart, Pie, Cell, Sector } from "recharts";
import { useParams } from "react-router-dom";
import axios from "axios";

const resChart = () => {
  const id = useParams();
  const [res, setRes] = useState(false);

  useEffect(() => {
    const result = axios
      .get(`/api/user/` + id.id)
      .then(result => {
        setTimeout(() => {
          console.log(result.data.data.research_value);
          setRes(result.data.data.research_value);
        }, 1000);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const data = [
    {
      name: "example1",
      value: 0.8
    },
    {
      name: "example2",
      value: 0.2
    }
  ];

  const COLORS = ["#0088FE", "#FFF", "#FFBB28", "#FF8042"];

  if (!res)
  return (
    <Fragment>
      <div class="alert alert-info" role="alert">
        Currently there is no data to display.
      </div>
    </Fragment>
  );
  
  return (
    <Fragment>
      <h2 className="text-center">Research Chart</h2>
      <ResponsiveContainer height={350} width="100%">
        <PieChart>
          <Pie
            data={res}
            dataKey="value"
            nameKey="name"
            startAngle={-180}
            endAngle={180}
            label
            outerRadius={120}
          >
            {data.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Pie>
        </PieChart>
      </ResponsiveContainer>
    </Fragment>
  );
};

export default resChart;
