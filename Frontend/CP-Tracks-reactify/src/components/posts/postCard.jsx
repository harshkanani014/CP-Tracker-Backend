import React from "react";

import "./postCard.css";

export default function PostCard({ cardInfo }) {
  return (
    <div className="col-md-4">
      <div className="card shadow">
        <div className="inner">
          <img className="card-img-top" src={cardInfo.image} alt={cardInfo.alt} />
        </div>

        <div className="card-body">
          <h4 className="card-title">{cardInfo.heading}</h4>
          <p className="card-text">{cardInfo.text}</p>
          <a href="#" className="btn btn-success">
            Practise
          </a>
        </div>
      </div>
    </div>
  );
}
