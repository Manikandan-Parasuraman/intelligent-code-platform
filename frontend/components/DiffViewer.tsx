"use client";

export default function DiffViewer({ oldCode, newCode, onApprove, onReject }) {
    const oldLines = oldCode.split("\n");
    const newLines = newCode.split("\n");

    return (
        <div style={{ padding: 10, background: "#1e1e1e", color: "white" }}>
            <h3>🔍 Code Diff</h3>

            <div style={{ display: "flex", gap: 10 }}>
                {/* OLD CODE */}
                <pre style={{ flex: 1, background: "#2d2d2d", padding: 10 }}>
                    {oldLines.map((line, i) => (
                        <div key={i} style={{ color: "#f87171" }}>
                            - {line}
                        </div>
                    ))}
                </pre>

                {/* NEW CODE */}
                <pre style={{ flex: 1, background: "#2d2d2d", padding: 10 }}>
                    {newLines.map((line, i) => (
                        <div key={i} style={{ color: "#4ade80" }}>
                            + {line}
                        </div>
                    ))}
                </pre>
            </div>

            <div style={{ marginTop: 10 }}>
                <button onClick={onApprove}>✅ Approve</button>
                <button onClick={onReject} style={{ marginLeft: 10 }}>
                    ❌ Reject
                </button>
            </div>
        </div>
    );
}