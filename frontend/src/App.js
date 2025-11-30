import React, { useEffect, useRef, useState } from "react";
import "./App.css";

const API_BASE = "http://localhost:8000";

function useDebounce(value, delay = 600) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value]);
  return debounced;
}

export default function App() {
  const [roomId, setRoomId] = useState("");
  const [connectedRoom, setConnectedRoom] = useState("");
  const [code, setCode] = useState("");
  const [suggestion, setSuggestion] = useState("");

  const debouncedCode = useDebounce(code);
  const wsRef = useRef(null);

  async function createRoom() {
    const res = await fetch(`${API_BASE}/rooms`, { method: "POST" });
    const data = await res.json();
    setRoomId(data.roomId);
    joinRoom(data.roomId);
  }

  function joinRoom(id) {
    if (!id) return;

    const ws = new WebSocket(`ws://localhost:8000/ws/${id}`);

    ws.onopen = () => {
      setConnectedRoom(id);
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === "sync" || data.type === "edit") {
        setCode(data.code);
      }
    };

    wsRef.current = ws;
  }

  function onCodeChange(v) {
    setCode(v);

    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(
        JSON.stringify({ type: "edit", code: v })
      );
    }
  }

  useEffect(() => {
    if (!connectedRoom) return;

    async function fetchSuggestion() {
      const res = await fetch(`${API_BASE}/autocomplete`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          code,
          cursorPosition: code.length,
          language: "python",
        }),
      });

      const data = await res.json();
      setSuggestion(data.suggestion);
    }

    fetchSuggestion();
  }, [debouncedCode]);

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">Real-Time Pair Programming</h1>

        <div className="room-controls">
          <button className="btn primary" onClick={createRoom}>
            + Create Room
          </button>

          <input
            className="input"
            placeholder="Room ID"
            value={roomId}
            onChange={(e) => setRoomId(e.target.value)}
          />

          <button className="btn" onClick={() => joinRoom(roomId)}>
            Join
          </button>
        </div>

        {connectedRoom && (
          <div className="badge">
            Connected • Room <b>{connectedRoom}</b>
          </div>
        )}

        <textarea
          className="editor"
          value={code}
          onChange={(e) => onCodeChange(e.target.value)}
        />

        <div className="suggestion-box">
          <span className="suggest-title">AI Suggestion:</span>
          <code>{suggestion}</code>
        </div>
      </div>
    </div>
  );
}
