"use client";
import { useState } from "react";

export default function ChatPanel({ setCode }) {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const API_URL = process.env.NEXT_PUBLIC_API_URL;
    const API_KEY = process.env.NEXT_PUBLIC_API_KEY;

    const sendMessage = async () => {
        if (!input) return;

        try {
            const res = await fetch(`${API_URL}/generate`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": API_KEY,
                },
                body: JSON.stringify({ question: input }),
            });

            if (!res.ok) {
                const err = await res.text();
                console.error("API ERROR:", err);
                return;
            }

            const data = await res.json();
            console.log("API RESPONSE:", data);

            setMessages((prev) => [
                ...prev,
                { role: "user", content: input },
                { role: "ai", content: JSON.stringify(data, null, 2) },
            ]);

            if (data.code) {
                setCode(data.code);
            }

            setInput("");
        } catch (err) {
            console.error("FETCH ERROR:", err);
        }
    };

    return (
        <div style={{ width: 300, display: "flex", flexDirection: "column" }}>
            <div style={{ flex: 1, overflowY: "auto" }}>
                {messages.map((m, i) => (
                    <div key={i}>
                        <b>{m.role}:</b>
                        <pre>{m.content}</pre>
                    </div>
                ))}
            </div>

            <div style={{ display: "flex" }}>
                <input
                    style={{ flex: 1 }}
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
}