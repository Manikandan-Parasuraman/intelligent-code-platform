import Editor from "@monaco-editor/react";

export default function CodeEditor({ code, setCode }) {
    return (
        <div style={{ flex: 1 }}>
            <Editor
                height="100%"
                defaultLanguage="python"
                value={code}
                onChange={(value) => setCode(value)}
                theme="vs-dark"
            />
        </div>
    );
}