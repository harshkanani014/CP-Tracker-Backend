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
      <div class="site-header w-100">
        <div id="carouselExample" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li
              data-target="#carouselExample"
              data-slide-to="0"
              class="active"
            ></li>
            <li data-target="#carouselExample" data-slide-to="1"></li>
            <li data-target="#carouselExample" data-slide-to="2"></li>
          </ol>

          <div class="carousel-inner">
            <div class="carousel-item active">
              <img
                src={require("../../assets/cp-carousel.png")} 
                alt="First Slide"
                class="d-block w-100"
              />
            </div>
            <div class="carousel-item">
              <img
               src={require("../../assets/python-carousel.png")}
                alt="Second Slide"
                class="d-block w-100"
              />
            </div>
            <div class="carousel-item">
              <img
                src={require("../../assets/cpp-carousel.png")}
                alt="Third Slide"
                class="d-block w-100"
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
