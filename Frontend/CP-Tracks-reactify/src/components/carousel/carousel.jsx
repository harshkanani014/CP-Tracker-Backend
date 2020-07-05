import React, { Component } from "react";

import Carousel from "nuka-carousel";

class CarouselMapped extends Component {
  render() {
    return (
      <Carousel autoplay="true" >
        <img src={require("../../assets/cp-carousel.png")} alt="Competitive Programming" />
        <img src={require("../../assets/python-carousel.png")} alt="Competitive Programming" />
        <img src={require("../../assets/cpp-carousel.png")} alt="Competitive Programming" />
      </Carousel>
    );
  }
}

/*
class CarouselMapped extends Component {
  render() {
    return (
      <div className="site-header w-100">
        <div id="carouselExample" className="carousel slide" data-ride="carousel">
          <ol className="carousel-indicators">
            <li
              data-target="#carouselExample"
              data-slide-to="0"
              className="active"
            ></li>
            <li data-target="#carouselExample" data-slide-to="1"></li>
            <li data-target="#carouselExample" data-slide-to="2"></li>
          </ol>

          <div className="carousel-inner">
            <div className="carousel-item active">
              <img
                src={require("../../assets/cp-carousel.png")} 
                alt="First Slide"
                className="d-block w-100"
              />
            </div>
            <div className="carousel-item">
              <img
               src={require("../../assets/python-carousel.png")}
                alt="Second Slide"
                className="d-block w-100"
              />
            </div>
            <div className="carousel-item">
              <img
                src={require("../../assets/cpp-carousel.png")}
                alt="Third Slide"
                className="d-block w-100"
              />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
*/
export default CarouselMapped;
