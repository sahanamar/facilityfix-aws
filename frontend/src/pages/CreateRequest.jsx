import { useState } from "react";
import API from "../api/requestApi";

function CreateRequest() {

  const [request, setRequest] = useState({
    title: "",
    description: "",
    priority: "LOW"
  });

  const submitRequest = async () => {

    await API.post("/requests", request);

    alert("Request Created");
  };

  return (
    <div>

      <h2>Create Maintenance Request</h2>

      <input
        placeholder="Title"
        onChange={(e) =>
          setRequest({
            ...request,
            title: e.target.value
          })
        }
      />

      <br /><br />

      <textarea
        placeholder="Description"
        onChange={(e) =>
          setRequest({
            ...request,
            description: e.target.value
          })
        }
      />

      <br /><br />

      <select
        onChange={(e) =>
          setRequest({
            ...request,
            priority: e.target.value
          })
        }
      >
        <option>LOW</option>
        <option>MEDIUM</option>
        <option>HIGH</option>
      </select>

      <br /><br />

      <button onClick={submitRequest}>
        Submit
      </button>

    </div>
  );
}

export default CreateRequest;