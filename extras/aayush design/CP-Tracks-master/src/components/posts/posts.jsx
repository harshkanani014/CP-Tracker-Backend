import React, { Component } from "react";

import PostCard from "./postCard.jsx";

class Posts extends Component {
  render() {
    return (
      <div class="container" id="practise">
        <div class="row justify-content-center justify-content-space-between">
          <PostCard
            cardInfo={{
              heading: "Competitive Programming",
              image: require("../../assets/cpcard.png"),
              alt: "Competitive Programming",
              text:
                "Get ready to practise and learn to compete! A track for mastering Competitive Programming. Happy Coding!",
            }}
          />{" "}
          ,
          <PostCard
            cardInfo={{
              heading: "Python Language Proficiency",
              image: require("../../assets/pycard.png"),
              alt: "Python Champion",
              text:
                "This track is for mastering Python. Follow this and become the master in Python.",
            }}
          />{" "}
          ,
          <PostCard
            cardInfo={{
              heading: "C++ Language Proficiency",
              image: require("../../assets/cppcard.png"),
              alt: "C++ Champion",
              text:
                "This track is for mastering C++. Follow this and become the master in C++.",
            }}
          />
        </div>
      </div>
    );
  }
}
export default Posts;
