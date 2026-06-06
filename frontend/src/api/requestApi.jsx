import axios from "axios";


const API = axios.create({
  // baseURL: "http://localhost:8000"
  baseURL: import.meta.env.VITE_API_URL
});

export default API;