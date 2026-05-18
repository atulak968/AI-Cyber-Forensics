import {
  LayoutDashboard,
  Link,
  Image,
  ShieldAlert,
  History,
  Settings,
} from "lucide-react";

export default function Sidebar() {

  const menu = [
    {
      title: "Dashboard",
      icon: <LayoutDashboard size={20} />,
    },
    {
      title: "URL Analysis",
      icon: <Link size={20} />,
    },
    {
      title: "OCR Analysis",
      icon: <Image size={20} />,
    },
    {
      title: "Threat Intel",
      icon: <ShieldAlert size={20} />,
    },
    {
      title: "History",
      icon: <History size={20} />,
    },
    {
      title: "Settings",
      icon: <Settings size={20} />,
    },
  ];

  return (

    <div className="h-screen w-64 bg-[#050816] border-r border-green-500/20 p-6 flex flex-col">

      {/* LOGO */}

      <div className="mb-10">

        <h1 className="text-3xl font-extrabold text-green-400">

          AI Cyber

        </h1>

        <p className="text-gray-400 text-sm">

          Forensics Platform

        </p>

      </div>

      {/* MENU */}

      <div className="flex flex-col gap-3">

        {menu.map((item, index) => (

          <button
            key={index}
            className="flex items-center gap-3 px-4 py-3 rounded-xl bg-transparent hover:bg-green-500/10 border border-transparent hover:border-green-500/20 transition-all text-gray-300 hover:text-green-400"
          >

            {item.icon}

            <span>{item.title}</span>

          </button>
        ))}
      </div>

      {/* SYSTEM STATUS */}

      <div className="mt-auto bg-black border border-green-500/20 rounded-2xl p-4">

        <p className="text-green-400 font-bold mb-2">

          SYSTEM STATUS

        </p>

        <div className="flex items-center gap-2">

          <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse" />

          <span className="text-gray-300">

            ONLINE

          </span>

        </div>

      </div>

    </div>
  );
}