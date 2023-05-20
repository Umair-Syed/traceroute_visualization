import React from "react";
import useWebSocket from 'react-use-websocket';
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

function App() {
  const [input, setInput] = React.useState("");
  const [socketUrl, setSocketUrl] = React.useState<string | null>(null);
  const [messageHistory, setMessageHistory] = React.useState<string[]>([]);

  const {
    sendMessage,
    lastMessage,
    readyState,
  } = useWebSocket(socketUrl, {
    onOpen: () => {
      console.log('Connection opened');
      if (input !== '') {
        sendMessage(JSON.stringify({ 'hostname': input }));
      }
    },
    onClose: () => console.log('Connection closed'),
    // Will attempt to reconnect on all close events, such as server shutting down
    shouldReconnect: (_) => true,
  });

  React.useEffect(() => {
    if (lastMessage !== null) {
      console.log('Received message: ', lastMessage.data);
      setMessageHistory((prev) => [...prev, lastMessage.data]);
    }
  }, [lastMessage]);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInput(event.target.value);    
  };

  const handleRunClick = () => {
    setSocketUrl('ws://127.0.0.1:8000/ws/traceroute/');
  };

  React.useEffect(() => {
    // Cleanup function
    return () => {
      // Disconnect the WebSocket
      console.log('Disconnecting WebSocket');
      setSocketUrl(null);
    };
  }, []);

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
          className="btn run-btn"
          onClick={handleRunClick}
        >
          Run
        </button>
      </div>
      <div>
        <h2>Results:</h2>
        {messageHistory.map((message, idx) => (
          <div key={idx}>
            {message}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
