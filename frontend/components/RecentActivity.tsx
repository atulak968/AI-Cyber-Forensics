"use client";

import { useEffect, useState } from "react";

const API = process.env.NEXT_PUBLIC_API_URL;

export default function RecentActivity() {

  const [history, setHistory] = useState<any[]>([]);

  const [loading, setLoading] = useState(true);

  const fetchHistory = async () => {

    try {

      const response = await fetch(
        `${API}/history`
      );

      if (!response.ok) {
        throw new Error("Failed to fetch history");
      }

      const data = await response.json();

      console.log("HISTORY:", data);

      if (Array.isArray(data)) {
        setHistory(data);
      } else {
        setHistory([]);
      }

    } catch (error) {

      console.error("HISTORY ERROR:", error);

      setHistory([]);

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchHistory();

  }, []);

  return (

    <div className="mt-10 bg-zinc-950 border border-zinc-800 rounded-2xl p-6 shadow-2xl">

      <h2 className="text-2xl font-bold text-cyan-400 mb-6">

        Recent Threat Activity

      </h2>

      {loading && (

        <p className="text-zinc-400">
          Loading activity...
        </p>
      )}

      {!loading && history.length === 0 && (

        <p className="text-zinc-500">
          No recent activity found.
        </p>
      )}

      <div className="flex flex-col gap-4">

        {history.map((item, index) => (

          <div
            key={item?.id || index}
            className={`p-4 rounded-xl border flex justify-between items-center ${
              item?.prediction === "PHISHING" ||
              item?.prediction === "SCAM"

                ? "bg-red-950 border-red-500"

                : "bg-green-950 border-green-500"
            }`}
          >

            <div>

              <p className="font-bold text-lg">

                {item?.prediction || "UNKNOWN"}

              </p>

              <p className="text-sm text-zinc-400">

                {item?.analysis_type || "Unknown"}

              </p>

            </div>

            <div className="text-right">

              <p className="text-sm text-zinc-300">

                {item?.confidence
                  ? (item.confidence * 100).toFixed(2)
                  : "0.00"}%

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