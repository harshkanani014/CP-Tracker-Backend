import React, { Component } from 'react';
import "./footer.css";


class Footer extends Component {
  state = { 
    creators: [
      {name:"Jainam Desai", linkedin:"https://in.linkedin.com/in/jainam-desai"},
      {name:"Harsh Kanani", linkedin:"https://in.linkedin.com/in/harsh-kanani-69a45818"},
      {name:"Ayush Chodvadyia", linkedin:"https://in.linkedin.com/in/aayush-chodvadiya-9122b418b"}
    ]
   }
  render() { 
    return ( 
      <footer>
        <ul>
          {this.state.creators.map(creator => <li class="list-group-item d-flex justify-content-between align-items-center" key={creator}>
            {creator.name}
            <i className="fa fa-linkedin" href={creator.linkedin} >Linkedin</i>
          </li>)}
        </ul>
      </footer>
     );
  }
}
 
export default Footer;