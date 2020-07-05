import React, { Component } from "react";
import "./header.css";

class Header extends Component {
  render() {
    return (
      <div className="header">
        <div className="logo">
          <img src={require("../../assets/logo.png")} alt="logo" width="40" />
        </div>
        <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
        <div className="search">
          <form className="form-inline my-2 my-lg-0">
            <input
              className="form-control mr-sm-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button className="btn btn-outline-success my-2 my-sm-0" type="submit">
              Search
            </button>
          </form>
        </div>
      </div>
    );
  }
}

export default Header;
