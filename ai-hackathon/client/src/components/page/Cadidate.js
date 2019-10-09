import React, {Fragment} from 'react'
import EduChart from '../chart-widget/eduChart';
import SentiChart from '../chart-widget/sentiChart';
import SkillChart from '../chart-widget/skillChart';
import ResChart from '../chart-widget/resChart';

const Candidate = () => {
  return (
    <Fragment>
      <div className="row charts-wrapper">
        <div className="col-12 col-md-6">
          <EduChart />
        </div>
        <div className="col-12 col-md-6">
          <SentiChart />
        </div>
        <div className="col-12 col-md-6">
          <SkillChart />
        </div>
        <div className="col-12 col-md-6">
          <ResChart />
        </div>
      </div>
    </Fragment>
  )
}

export default Candidate
