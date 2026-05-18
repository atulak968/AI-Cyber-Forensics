export default function Navbar() {

  return (

    <div className="w-full h-20 border-b border-green-500/20 bg-[#050816] flex items-center justify-between px-8">

      <div>

        <h1 className="text-3xl font-bold text-green-400">

          AI Cyber Forensics

        </h1>

        <p className="text-gray-400 text-sm">

          Advanced Fraud Intelligence Dashboard

        </p>

      </div>

      <div className="flex items-center gap-6">

        <div className="bg-black border border-green-500/20 rounded-xl px-4 py-2">

          <p className="text-green-400 font-bold">

            SYSTEM ONLINE

          </p>

        </div>

        <div className="bg-black border border-green-500/20 rounded-xl px-4 py-2">

          <p className="text-gray-300">

            Investigator

          </p>

        </div>

      </div>

    </div>
  );
}