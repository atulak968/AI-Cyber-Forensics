"use client";

import { useEffect, useState } from "react";

export default function RecentActivity() {

  const [history, setHistory] = useState<any[]>([]);

  const [loading, setLoading] = useState(true);

  // -------------------------
  // FETCH HISTORY
  // -------------------------

  const fetchHistory = async () => {

    try {

      const response = await fetch(

        "http://127.0.0.1:8000/history"
      );

      const data = await response.json();

      setHistory(data || []);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  // -------------------------
  // LOAD ON START
  // -------------------------

  useEffect(() => {

    fetchHistory();

  }, []);

  return (

    <div className="mt-10 bg-zinc-950 border border-zinc-800 rounded-2xl p-6 shadow-2xl">

      <h2 className="text-2xl font-bold text-cyan-400 mb-6">

        Recent Threat Activity

      </h2>

      {/* ------------------------- */}
      {/* LOADING */}
      {/* ------------------------- */}

      {loading && (

        <p className="text-zinc-400">

          Loading activity...
        </p>
      )}

      {/* ------------------------- */}
      {/* EMPTY */}
      {/* ------------------------- */}

      {!loading && history.length === 0 && (

        <p className="text-zinc-500">

          No recent activity found.
        </p>
      )}

      {/* ------------------------- */}
      {/* HISTORY LIST */}
      {/* ------------------------- */}

      <div className="flex flex-col gap-4">

        {history.map((item) => (

          <div

            key={item.id}

            className={`p-4 rounded-xl border flex justify-between items-center ${
              item.prediction === "PHISHING" ||
              item.prediction === "SCAM"

                ? "bg-red-950 border-red-500"

                : "bg-green-950 border-green-500"
            }`}
          >

            <div>

              <p className="font-bold text-lg">

                {item.prediction}

              </p>

              <p className="text-sm text-zinc-400">

                {item.analysis_type}

              </p>

            </div>

            <div className="text-right">

              <p className="text-sm text-zinc-300">

                {(item.confidence * 100).toFixed(2)}%
              </p>

              <p className="text-xs text-zinc-500">

                Confidence
              </p>

            </div>

          </div>
        ))}
      </div>
    </div>
  );
}