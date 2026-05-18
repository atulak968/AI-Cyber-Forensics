import {
  ShieldAlert,
  ShieldCheck,
  Database,
  Activity,
} from "lucide-react";

export default function StatsCards() {

  const stats = [
    {
      title: "Total Analyses",
      value: "1,248",
      icon: <Activity className="text-green-400" />,
    },
    {
      title: "Threats Detected",
      value: "342",
      icon: <ShieldAlert className="text-red-500" />,
    },
    {
      title: "Accuracy",
      value: "98.12%",
      icon: <ShieldCheck className="text-green-400" />,
    },
    {
      title: "Data Processed",
      value: "2.45 GB",
      icon: <Database className="text-purple-400" />,
    },
  ];

  return (

    <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

      {stats.map((stat, index) => (

        <div
          key={index}
          className="bg-[#050816] border border-green-500/20 rounded-2xl p-6 shadow-lg shadow-green-500/5"
        >

          <div className="flex items-center justify-between mb-4">

            <p className="text-gray-400">

              {stat.title}

            </p>

            {stat.icon}

          </div>

          <h2 className="text-3xl font-bold text-white">

            {stat.value}

          </h2>

        </div>
      ))}
    </div>
  );
}