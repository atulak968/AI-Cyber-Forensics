
import RecentActivity from "@/components/RecentActivity";
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";
import StatsCards from "@/components/StatsCards";
import AnalyzePanel from "@/components/AnalyzePanel";
import OCRUpload from "@/components/OCRUpload";
import URLAnalyzer from "@/components/URLAnalyzer";

export default function Home() {

  return (

    <main className="flex bg-black min-h-screen text-white">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-8">

          <StatsCards />

          <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

            <AnalyzePanel />

            <OCRUpload />

            <URLAnalyzer />

          </div>

          <RecentActivity />

        </div>

      </div>

    </main>
  );
}