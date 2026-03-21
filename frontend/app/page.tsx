"use client";

import { useState } from "react";
import Sidebar from "../components/Sidebar";
import Editor from "../components/Editor";
import ChatPanel from "../components/ChatPanel";

export default function Home() {
    const [code, setCode] = useState("// Select file or ask AI...");

    return (
        <div style={{ display: "flex", height: "100vh" }}>
            <Sidebar setCode={setCode} />
            <Editor code={code} setCode={setCode} />
            <ChatPanel setCode={setCode} />
        </div>
    );
}