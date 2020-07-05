import React from "react";
import "./footer.css";

export default function Footer() {
  return (
    <footer>
      <div class="content-3">
        <div class="container p-4">
          <div class="footer border-top">
            <div class="row">
              <div class="col-3">
                <div class="d-flex flex-column">
                  <h6 class="text-white">Creators</h6>
                  <ul class="text-white">
                    <li>
                      <a href="https://www.linkedin.com/in/harsh-kanani-69a45818b/">
                        Harsh Kannani
                      </a>
                    </li>
                    <li>
                      <a href="https://www.linkedin.com/in/jainam-desai/">
                        Jainam Desai
                      </a>
                    </li>
                    <li>
                      <a href="https://www.linkedin.com/in/aayush-chodvadiya/">
                        Aayush Chodvadiya
                      </a>
                    </li>
                  </ul>
                </div>
              </div>

              <div class="col-3">
                <div class="d-flex flex-column">
                  <h6 class="text-white">Community</h6>
                  <a href="">Home</a>
                  <a href="#practise">Practise</a>
                  <a href="#about">About Us</a>
                  <a href="">Blog</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
