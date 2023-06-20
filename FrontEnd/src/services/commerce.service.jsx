import axios from "axios";

const URL = "https://jsonplaceholder.typicode.com"

export const getDatas = () => {

    return axios.get(URL + "/users");
};