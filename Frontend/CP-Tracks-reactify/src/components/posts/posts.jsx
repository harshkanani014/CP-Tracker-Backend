import React, { Component } from "react";

import PostCard from "./postCard.jsx";

class Posts extends Component {
  state = {
    posts: [
      {
        id: 1,
        cardInfo: {
          heading: "Competitive Programming",
          image: require("../../assets/cpcard.png"),
          alt: "Competitive Programming",
          text:
            "Get ready to practise and learn to compete! A track for mastering Competitive Programming. Happy Coding!",
        },
      },
      {
        id: 2,
        cardInfo: {
          heading: "Python Language Proficiency",
          image: require("../../assets/pycard.png"),
          alt: "Python Champion",
          text:
            "This track is for mastering Python. Follow this and become the master in Python.",
        },
      },
      {
        id: 3,
        cardInfo: {
          heading: "C++ Language Proficiency",
          image: require("../../assets/cppcard.png"),
          alt: "C++ Champion",
          text:
            "This track is for mastering C++. Follow this and become the master in C++.",
        },
      },
    ],
  };
  render() {
    return (
      <div className="container" id="practise">
        <div className="row justify-content-center justify-content-space-between">
          {this.state.posts.map(post => <PostCard key={post.id} cardInfo={post.cardInfo}/>)}
        </div>
      </div>
    );
  }
}
export default Posts;
