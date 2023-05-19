import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

function App() {
  const [input, setInput] = React.useState("");

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSearch = () => {
    // handle your search here
  };

  return (
    <div
      id="root"
      className="d-flex flex-column align-items-center justify-content-center"
    >
      <h1>Traceroute Visualization</h1>
      <div className="d-flex justify-content-center mt-5" style={{ gap: "0.5rem", width: '100%' }}>
        <input
          type="text"
          className="form-control"
          style={{ width: '40%' }}
          placeholder="Enter hostname"
          value={input}
          onChange={handleChange}
        />
        <button
          type="button"
          className="btn search-btn"
          onClick={handleSearch}
        >
          Run
        </button>
      </div>
    </div>
  );
}

export default App;
