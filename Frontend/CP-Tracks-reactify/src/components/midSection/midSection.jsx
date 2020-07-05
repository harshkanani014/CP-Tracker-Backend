import React from "react";

import "./midSection.css";

export default function MiddleGreeting () {
  return (
    <div className="content-2" id="about">
    <br />
    <div className="row text-center justify-content-center p-4">
      <div className="col-6 justify-content-center m-3">
        <h2>We help you to practise!</h2>
        <p>
          There is a lot of material out there for learning Coding. So don't
          worry. We have prepared different tracks for learning coding which
          covers all the necessary concepts and questions you have to do for
          mastering it.
        </p>
        <div className="row">
          <div className="col-6">
            <h4>Our Mission</h4>
            <p>
              To empower each and every student interested in coding with
              power to code.
            </p>
          </div>
          <div className="col-6">
            <h4>Our Vision</h4>
            <p>
              To grow this community and level up the coding enviornment that
              we have in today's world to next level.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  )
}