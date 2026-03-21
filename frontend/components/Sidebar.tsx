"use client";
import { useEffect, useState } from "react";

export default function Sidebar({ setCode }) {
    const [files, setFiles] = useState([]);

    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    useEffect(() => {
        fetch(`${API_URL}/files`)
            .then((res) => res.json())
            .then((data) => setFiles(data.files))
            .catch(console.error);
    }, []);

    const loadFile = async (file) => {
        const res = await fetch(`${API_URL}/file?name=${file}`);
        const data = await res.json();
        setCode(data.content);
    };

    return (
        <div style={{ width: 200, background: "#252526", padding: 10 }}>
            <h4>📂 Files</h4>
            <ul>
                {files.map((file, i) => (
                    <li key={i} onClick={() => loadFile(file)} style={{ cursor: "pointer" }}>
                        {file}
                    </li>
                ))}
            </ul>
        </div>
    );
}