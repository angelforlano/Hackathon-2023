import React, { useState, useEffect } from "react";
import Filter from "../../assets/images/filtro.png";
import Card from 'react-bootstrap/Card';
import dataShops from '../../data/Data.json';
import "./Search.css"
{/*import { getDatas } from "../../services/commerce.service";*/}

const Search = () => {
  //set hooks useState
  const [shops, setShops] = useState([]);
  const [search, setSearch] = useState("");

{/*  const showData = async () => {
    const {data} = await getDatas();
    console.log(data);
    setShops(data)
  };*/}
  
  
//search function
const searcher = (e) => {
  setSearch(e.target.value)
  //console.log(e.target.value)
}

//filter method 
 const results = !search ? shops : shops.filter((dato)=> dato.localName.toLowerCase().includes(search.toLocaleLowerCase())
        );
  
 useEffect( ()=> {
  setShops(dataShops);
}, []);

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

      <section className="cards">
        {results.map((shop) => (
        <Card className="card-shop" style={{ width: '18rem' }} key={shop.id}>
          <Card.Body>
            <Card.Title>{shop.localName}</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">{shop.districtName}</Card.Subtitle>
            <Card.Text>
              {shop.neighbourhoodName}
            </Card.Text>
            <Card.Link href="#">Contacte del comerç</Card.Link>
          </Card.Body>
        </Card>
        ))}
      </section>
    </div>
  );
};

export default Search;
