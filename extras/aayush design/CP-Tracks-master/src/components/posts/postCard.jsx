import React from "react";

import "./postCard.css";

export default function PostCard({ cardInfo }) {
  return (
    <div class="col-md-4">
      <div class="card shadow">
        <div class="inner">
          <img class="card-img-top" src={cardInfo.image} alt={cardInfo.alt} />
        </div>

        <div class="card-body">
          <h4 class="card-title">{cardInfo.heading}</h4>
          <p class="card-text">{cardInfo.text}</p>
          <a href="#" class="btn btn-success">
            Practise
          </a>
        </div>
      </div>
    </div>
  );
}
