import React from "react";
import { useState } from "react";
import API from "../api/requestApi";

function AssignRequest() {

  const [requestId, setRequestId] =
    useState("");

  const [technicianId, setTechnicianId] =
    useState("");

  const assign = async () => {

    await API.put(
      `/requests/${requestId}/assign`,
      {
        technician_id: technicianId
      }
    );

    alert("Assigned");
  };

  return (
    <div>

      <h2>Assign Technician</h2>

      <input
        placeholder="Request Id"
        onChange={(e) =>
          setRequestId(e.target.value)
        }
      />

      <br /><br />

      <input
        placeholder="Technician Id"
        onChange={(e) =>
          setTechnicianId(e.target.value)
        }
      />

      <br /><br />

      <button onClick={assign}>
        Assign
      </button>

    </div>
  );
}

export default AssignRequest;