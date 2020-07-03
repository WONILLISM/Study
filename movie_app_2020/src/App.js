import React from 'react';
import PropTypes from "prop-types";

function Food({name, picture, rating}){
  return <div>
    <h2>I like {name}</h2>
    <h4>{rating}/5.0</h4>
    <img src={picture} alt={name} />
  </div>
}

Food.propTypes = {
  name : PropTypes.string.isRequired,
  picture : PropTypes.string.isRequired,
  rating : PropTypes.number.isRequired 
}

const foodILike = [
  {
    id:"1",
    name: "Kimchi", 
    image:"https://okonomikitchen.com/wp-content/uploads/2020/03/vegan-kimchi-recipe-12-of-14.jpg",
    rating: 5
  },
  {
    id:"2",
    name: "Ramen", 
    image:"https://hips.hearstapps.com/hmg-prod/images/190208-delish-ramen-horizontal-093-1550096715.jpg",
    rating: 4.9
  },
  {
    id:"3",
    name: "Potato", 
    image:"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-191907-twice-baked-potatoes-0027-landscape-pf-1564166855.png?crop=0.668xw:1.00xh;0.289xw,0&resize=480:*",
    rating: 4.8
  },
]
function App() {
  return (
  <div>
    <h1>Hello!</h1> 
    { foodILike.map(dish => <Food 
        key={dish.id} 
        name={dish.name} 
        picture={dish.image} 
        rating={dish.rating}
        />)}
  </div>
  );
}

export default App;
