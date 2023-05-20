import React, { useState, useEffect } from 'react';
import useWebSocket from 'react-use-websocket';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

const webSocketOptions = {
  shouldReconnect: (closeEvent: CloseEvent) => closeEvent.code !== 1000, // Don't reconnect on normal closure
};

function App() {
  const [input, setInput] = useState('');
  const [socketUrl, setSocketUrl] = React.useState<string | null>(null);
  const [messageHistory, setMessageHistory] = React.useState<any[]>([]);
  const [tracerouteStatus, setTracerouteStatus] = useState('');

  const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl, webSocketOptions);

  useEffect(() => {
    if (lastMessage) {
      console.log('Received message: ', lastMessage.data);
      const jsonData = JSON.parse(lastMessage.data); // parse the data into JSON
      setMessageHistory((prev) => [...prev, jsonData]);
    }
  }, [lastMessage]);

  useEffect(() => {
    if (readyState === 1) {
      console.log('Connection opened', readyState);
      setTracerouteStatus('Running Traceroute...');
      if (input !== '') {
        sendMessage(JSON.stringify({ hostname: input }));
      }
    } else if (readyState === 3) {
      console.log('Connection closed');
      setTracerouteStatus('Traceroute Finished');
    }
  }, [readyState]);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInput(event.target.value);
  };

  const handleRunClick = () => {
    // Disconnect the existing WebSocket, if any
    setSocketUrl(null);
  
    // Clear the old traceroute results
    setMessageHistory([]);
    
    // Use a timeout to allow state updates to propagate
    setTimeout(() => {
      // Start a new WebSocket connection
      setSocketUrl('ws://127.0.0.1:8000/ws/traceroute/');
    }, 100);
  };
  

  return (
    <div id="root" className="d-flex flex-column align-items-center justify-content-center">
      <h1>Traceroute Visualization</h1>
      <div className="d-flex justify-content-center mt-5" style={{ gap: '0.5rem', width: '100%' }}>
        <input
          type="text"
          className="form-control"
          style={{ width: '40%' }}
          placeholder="Enter hostname"
          value={input}
          onChange={handleChange}
        />
        <button type="button" className="btn run-btn" onClick={handleRunClick}>
          Run
        </button>
      </div>
      <div className="mt-5">
        <h4 className={tracerouteStatus === 'Running Traceroute...' ? "text-warning" : "text-success"}>{tracerouteStatus}</h4>
        {messageHistory.length > 0 && (
          <table className="table table-bordered mt-4" style={{color: "white", borderColor: "white"}}>
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">IP</th>
                <th scope="col">Latitude</th>
                <th scope="col">Longitude</th>
                <th scope="col">City</th>
                <th scope="col">State</th>
                <th scope="col">Country</th>
              </tr>
            </thead>
            <tbody>
              {messageHistory.map((message, idx) => (
                <tr key={idx}>
                <th scope="row">{idx + 1}</th>
                <td className={message.ip ? '' : 'text-secondary'}>{message.ip || 'Private'}</td>
                <td className={(message.latitude !== null && message.longitude !== null && message.latitude !== 0) ? '' : 'text-secondary'}>
                  {(message.latitude !== null && message.longitude !== null && message.latitude !== 0) ? message.latitude : 'Private'}
                </td>
                <td className={(message.latitude !== null && message.longitude !== null && message.longitude !== 0) ? '' : 'text-secondary'}>
                  {(message.latitude !== null && message.longitude !== null && message.longitude !== 0) ? message.longitude : 'Private'}
                </td>
                <td className={message.city ? '' : 'text-secondary'}>{message.city || 'Private'}</td>
                <td className={message.state ? '' : 'text-secondary'}>{message.state || 'Private'}</td>
                <td className={message.country ? '' : 'text-secondary'}>{message.country || 'Private'}</td>
              </tr>                        
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}

export default App;
