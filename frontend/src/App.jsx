import { BrowserRouter, Routes, Route }
from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Requests from "./pages/Requests";
import CreateRequest from "./pages/CreateRequest";
import AssignRequest from "./pages/AssignRequest";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/requests"
          element={<Requests />}
        />

        <Route
          path="/create-request"
          element={<CreateRequest />}
        />

        <Route
          path="/assign-request"
          element={<AssignRequest />}
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;