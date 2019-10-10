import React, { Fragment, useState, useEffect } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import { useParams } from "react-router-dom";
import axios from "axios";

const sentiChart = () => {
  const id = useParams();
  const [senti, setSenti] = useState(false);

  useEffect(() => {
    const result = axios
      .get(`/api/user/` + id.id)
      .then(result => {
        setTimeout(() => {
          console.log(result.data.data.sentimental_level);
          setSenti(result.data.data.sentimental_level);
        }, 1000);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  // const data = [
  //   {
  //     sentiValue: 0.87
  //   },
  //   {
  //     sentiValue: 0.8
  //   },
  //   {
  //     sentiValue: -0.2
  //   },
  //   {
  //     sentiValue: 0.38
  //   },
  //   {
  //     sentiValue: 0.45
  //   }
  // ];
  if (!senti)
  return (
    <Fragment>
      <div class="alert alert-info" role="alert">
        Currently there is no data to display.
      </div>
    </Fragment>
  );
  
  return (
    <Fragment>
      <h2 className="text-center">Sentimental Level</h2>
      <ResponsiveContainer height={350} width="100%">
        <LineChart data={senti}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis hide />
          <YAxis domain={[-1, 1]} />
          <Tooltip />
          <Line type="monotone" dataKey="sentiValue" />
        </LineChart>
      </ResponsiveContainer>
    </Fragment>
  );
};

export default sentiChart;
