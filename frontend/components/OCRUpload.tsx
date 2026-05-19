"use client";

import { useState } from "react";

import {
  UploadCloud,
  ShieldAlert,
  ShieldCheck,
} from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL;

export default function OCRUpload() {

  console.log("OCR API:", API);

  const [file, setFile] = useState<File | null>(null);

  const [result, setResult] = useState<any>(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  // =========================
  // FILE SELECT
  // =========================

  const handleFileChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {

    if (e.target.files?.[0]) {

      setFile(e.target.files[0]);

      setError("");

      setResult(null);
    }
  };

  // =========================
  // ANALYZE IMAGE
  // =========================

  const analyzeImage = async () => {

    if (!file) {

      setError("Please upload an image.");

      return;
    }

    setLoading(true);

    setError("");

    setResult(null);

    try {

      const formData = new FormData();

      formData.append("file", file);

      const response = await fetch(

        `${API}/analyze-image`,

        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {

        throw new Error(
          "OCR API request failed"
        );
      }

      const data = await response.json();

      console.log("OCR RESPONSE:", data);

      setResult(data);

    } catch (err: any) {

      console.error("OCR ERROR:", err);

      setError(
        err.message ||
        "Something went wrong."
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="bg-[#050816] border border-green-500/20 rounded-2xl p-6">

      <h2 className="text-2xl font-bold text-green-400 mb-6">

        OCR Image Analysis

      </h2>

      {/* ========================= */}
      {/* UPLOAD */}
      {/* ========================= */}

      <label className="flex flex-col items-center justify-center border-2 border-dashed border-green-500/20 rounded-2xl h-64 cursor-pointer hover:border-green-400 transition-all">

        <UploadCloud
          size={70}
          className="text-green-400 mb-4"
        />

        <p className="text-lg text-gray-300">

          Upload Scam Screenshot

        </p>

        <p className="text-sm text-gray-500 mt-2">

          JPG, PNG Supported

        </p>

        <input
          type="file"
          className="hidden"
          accept="image/*"
          onChange={handleFileChange}
        />

      </label>

      {/* ========================= */}
      {/* FILE INFO */}
      {/* ========================= */}

      {file && (

        <div className="mt-4 bg-black border border-green-500/20 rounded-xl p-3">

          <p className="text-green-400">

            Selected File

          </p>

          <p className="text-gray-300">

            {file.name}

          </p>

        </div>
      )}

      {/* ========================= */}
      {/* BUTTON */}
      {/* ========================= */}

      <button
        onClick={analyzeImage}
        disabled={loading}
        className="w-full mt-6 bg-green-500 hover:bg-green-600 transition-all text-black font-bold py-4 rounded-xl disabled:opacity-50"
      >

        {loading
          ? "Analyzing Image..."
          : "Analyze Screenshot"}

      </button>

      {/* ========================= */}
      {/* ERROR */}
      {/* ========================= */}

      {error && (

        <div className="mt-4 bg-red-950 border border-red-500 rounded-xl p-4">

          <p className="text-red-300">

            {error}

          </p>

        </div>
      )}

      {/* ========================= */}
      {/* RESULT */}
      {/* ========================= */}

      {result && (

        <div className="mt-6 border border-green-500/20 rounded-2xl p-5 bg-black">

          <div className="flex items-center gap-4 mb-4">

            {result.prediction === "SCAM IMAGE" ? (

              <ShieldAlert
                size={60}
                className="text-red-500"
              />

            ) : (

              <ShieldCheck
                size={60}
                className="text-green-400"
              />
            )}

            <div>

              <h2 className="text-3xl font-bold">

                {result.prediction || "UNKNOWN"}

              </h2>

              <p className="text-gray-400">

                OCR Threat Result

              </p>

            </div>

          </div>

          {/* ========================= */}
          {/* CONFIDENCE */}
          {/* ========================= */}

          <div className="mb-4">

            <p className="mb-2">

              Confidence Score

            </p>

            <div className="w-full bg-gray-800 rounded-full h-4">

              <div
                className={`h-4 rounded-full ${
                  result.prediction ===
                  "SCAM IMAGE"
                    ? "bg-red-500"
                    : "bg-green-500"
                }`}
                style={{
                  width: `${
                    result.confidence
                      ? result.confidence * 100
                      : 0
                  }%`,
                }}
              />

            </div>

            <p className="mt-2 font-bold">

              {result.confidence
                ? (
                    result.confidence * 100
                  ).toFixed(2)
                : "0.00"}%

            </p>

          </div>

          {/* ========================= */}
          {/* OCR TEXT */}
          {/* ========================= */}

          <div className="bg-[#050816] border border-green-500/20 rounded-xl p-4 max-h-64 overflow-auto">

            <p className="text-green-400 mb-2">

              Extracted OCR Text

            </p>

            <p className="text-gray-300 whitespace-pre-wrap">

              {result.extracted_text ||
                "No OCR text extracted."}

            </p>

          </div>

        </div>
      )}

    </div>
  );
}