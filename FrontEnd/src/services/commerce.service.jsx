import axios from "axios";

const URL = "https://localhost:8080/api"

export const getDatas = () => {

    return axios.get(URL + "/sector");
};