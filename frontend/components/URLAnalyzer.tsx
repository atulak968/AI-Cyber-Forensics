"use client";

import { useState } from "react";

const API = process.env.NEXT_PUBLIC_API_URL;

export default function URLAnalyzer() {

  console.log("API URL:", API);

  const [url, setUrl] = useState("");

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState<any>(null);

  const analyzeURL = async () => {

    if (!url) return;

    setLoading(true);

    setResult(null);

    try {

      const response = await fetch(

        `${API}/analyze-url`,

        {

          method: "POST",

          headers: {

            "Content-Type": "application/json",
          },

          body: JSON.stringify({

            url,
          }),
        }
      );

      const data = await response.json();

      console.log("API RESPONSE:", data);

      setResult(data);

    } catch (error) {

      console.log("FETCH ERROR:", error);

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="bg-zinc-950 border border-zinc-800 rounded-2xl p-6 shadow-2xl">

      <h2 className="text-2xl font-bold mb-4 text-cyan-400">

        URL Threat Analyzer

      </h2>

      <input
        type="text"
        placeholder="Enter suspicious URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="w-full bg-black border border-zinc-700 rounded-xl px-4 py-3 text-white outline-none focus:border-cyan-400"
      />

      <button
        onClick={analyzeURL}
        className="mt-4 w-full bg-cyan-500 hover:bg-cyan-400 text-black font-bold py-3 rounded-xl transition-all"
      >
        {loading ? "Analyzing..." : "Analyze URL"}
      </button>

      {result && (

        <div className="mt-6">

          <div
            className={`p-4 rounded-xl border text-center ${
              result.prediction === "PHISHING"
                ? "bg-red-950 border-red-500"
                : "bg-green-950 border-green-500"
            }`}
          >

            <h3 className="text-2xl font-bold">

              {result.prediction}

            </h3>

            <p className="mt-2 text-zinc-300">

              Confidence:{" "}
              {(result.confidence * 100).toFixed(2)}%

            </p>

            <p className="mt-2 text-sm text-zinc-400">

              Detection Source: {result.source}

            </p>

          </div>

        </div>
      )}
    </div>
  );
}