import React, { useState, useEffect } from "react";
import Table from 'react-bootstrap/Table';
import Filter from "../../assets/images/filtro.png";
import Card from 'react-bootstrap/Card';
import "./Search.css"
import { getDatas } from "../../services/commerce.service";

const Search = () => {
  //set hooks useState
  const [shops, setShops] = useState([]);
  const [search, setSearch] = useState("");

  const showData = async () => {
    const {data} = await getDatas();
    console.log(data);
    setShops(data)
  };
  
  
//search function
const searcher = (e) => {
  setSearch(e.target.value)
  //console.log(e.target.value)
}

//filter method 
 const results = !search ? shops : shops.filter((dato)=> dato.name.toLowerCase().includes(search.toLocaleLowerCase()))
  
 useEffect( ()=> {
  showData()
}, [])

  //view render

  return (
    <div>
      <div className="searcher-space">
        <div className="search">
          <input value={search} onChange={searcher} type="text" className="form-control searcher" />
          <img className="filter" src={Filter}/>  
        </div>
        <p>Prova amb 'Veterinari'</p>
      </div>

      <section>
        {results.map((shop) => (
        <Card style={{ width: '18rem' }} key={shop.id}>
          <Card.Body>
            <Card.Title>{shop.name}</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">{shop.username}</Card.Subtitle>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Card.Link href="#">Card Link</Card.Link>
            <Card.Link href="#">Another Link</Card.Link>
          </Card.Body>
        </Card>
        ))}
      </section>
    </div>
  );
};

export default Search;
