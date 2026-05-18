"use client";

import { useState } from "react";

import {
  ShieldAlert,
  ShieldCheck,
} from "lucide-react";
const API = process.env.NEXT_PUBLIC_API_URL;
export default function AnalyzePanel() {

  const [message, setMessage] = useState("");

  const [result, setResult] = useState<any>(null);

  const [loading, setLoading] = useState(false);

  // -------------------------
  // ANALYZE MESSAGE
  // -------------------------

  const analyzeThreat = async () => {

    setLoading(true);

    try {

      const response = await fetch(
        `${API}/detect`,
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            text: message,
          }),
        }
      );

      const data = await response.json();

      setResult(data);

    } catch (error) {

      console.error(error);
    }

    setLoading(false);
  };

  return (

    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

      {/* LEFT PANEL */}

      <div className="bg-[#050816] border border-green-500/20 rounded-2xl p-6">

        <h2 className="text-2xl font-bold text-green-400 mb-4">

          Analyze Text / Message

        </h2>

        <textarea
          className="w-full h-56 bg-black border border-green-500/20 rounded-xl p-4 text-lg focus:outline-none"
          placeholder="Paste suspicious message here..."
          value={message}
          onChange={(e) =>
            setMessage(e.target.value)
          }
        />

        <button
          onClick={analyzeThreat}
          className="w-full mt-6 bg-green-500 hover:bg-green-600 transition-all text-black font-bold py-4 rounded-xl"
        >
          {loading
            ? "Analyzing..."
            : "Analyze Threat"}
        </button>

      </div>

      {/* RIGHT PANEL */}

      <div className="bg-[#050816] border border-green-500/20 rounded-2xl p-6">

        <h2 className="text-2xl font-bold text-green-400 mb-6">

          Threat Intelligence

        </h2>

        {!result && (

          <div className="flex items-center justify-center h-64 text-gray-500">

            Awaiting Analysis...

          </div>
        )}

        {result && (

          <div>

            {/* STATUS */}

            <div className="flex items-center gap-4 mb-6">

              {result.prediction === "SCAM" ? (

                <ShieldAlert
                  size={70}
                  className="text-red-500"
                />

              ) : (

                <ShieldCheck
                  size={70}
                  className="text-green-400"
                />
              )}

              <div>

                <h2 className="text-4xl font-bold">

                  {result.prediction}

                </h2>

                <p className="text-gray-400">

                  Threat Analysis Result

                </p>

              </div>

            </div>

            {/* CONFIDENCE */}

            <div className="mb-6">

              <p className="mb-2 text-lg">

                Confidence Score

              </p>

              <div className="w-full bg-black rounded-full h-5">

                <div
                  className={`h-5 rounded-full ${
                    result.prediction ===
                    "SCAM"
                      ? "bg-red-500"
                      : "bg-green-500"
                  }`}
                  style={{
                    width: `${
                      result.confidence *
                      100
                    }%`,
                  }}
                />

              </div>

              <p className="mt-3 text-2xl font-bold">

                {(
                  result.confidence * 100
                ).toFixed(2)}%

              </p>

            </div>

            {/* INPUT */}

            <div className="bg-black border border-green-500/20 rounded-xl p-4">

              <p className="text-gray-400 mb-2">

                Message Content

              </p>

              <p className="text-lg">

                {result.input}

              </p>

            </div>

          </div>
        )}

      </div>

    </div>
  );
}