import React from "react";
import { useEffect, useState } from "react";
import API from "../api/requestApi";

function Requests() {

  const [requests, setRequests] = useState([]);

  useEffect(() => {
    loadRequests();
  }, []);

  const loadRequests = async () => {

    const response =
      await API.get("/requests");

    setRequests(response.data);
  };

  return (
    <div>

      <h2>Requests</h2>

      {requests.map((r) => (

        <div
          key={r.id}
          style={{
            border: "1px solid gray",
            margin: 10,
            padding: 10
          }}
        >
          <h3>{r.title}</h3>

          <p>{r.description}</p>

          <p>Status: {r.status}</p>

          <p>Priority: {r.priority}</p>

        </div>
      ))}

    </div>
  );
}

export default Requests;