import React, {useState, useEffect} from 'react';
import './Search.css';
import "bootstrap/dist/css/bootstrap.min.css";

const Search = () => {
//set hooks useState
const [ shops, setShops ] = useState([]);
const [ search, setSearch ] = useState("");


//function to get API
const URL = 'https://jsonplaceholder.typicode.com/users'

const showData = async () => {
 const response = await fetch(URL)
 const data = await response.json()
 console.log(data)
}
showData()
//filter method

//search function

  return (
    <div>Search</div>
  )
}

export default Search