import React from "react";
import "./App.css";

import Header from "./components/header/header";
import CarouselMapped from "./components/carousel/carousel.jsx";
import Posts from "./components/posts/posts.jsx";
import MiddleGreeting from "./components/midSection/midSection.jsx";
import Footer from "./components/footer/footer.jsx";

function App() {
  return (
    <div className="App">
      <Header />
      <CarouselMapped />
      <Posts />
      <MiddleGreeting />
      <Footer />
    </div>
  );
}

export default App;
