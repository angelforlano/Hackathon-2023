import React, { useState, useEffect } from "react";
import Table from 'react-bootstrap/Table';
import Filter from "../../assets/images/filtro.png";
import "./Search.css"

const Search = () => {
  //set hooks useState
  const [shops, setShops] = useState([]);
  const [search, setSearch] = useState("");

  //function to get API
  const URL = "https://jsonplaceholder.typicode.com/users";

  const showData = async () => {
    const response = await fetch(URL);
    const data = await response.json();
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

      <Table striped bordered hover>
        <thead>
          <tr>
            <th>NAME</th>
            <th>USER NAME</th>
          </tr>
        </thead>
        <tbody>
          {results.map((shop) => (
            <tr key={shop.id}>
              <td>{shop.name}</td>
              <td>{shop.username}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Search;
