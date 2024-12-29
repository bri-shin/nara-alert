'use client';

interface StatusCardProps {
  isRunning: boolean;
  onRefresh: () => void;
}

export default function StatusCard({ isRunning, onRefresh }: StatusCardProps) {
  const toggleScraper = async () => {
    try {
      await fetch('/api/toggle', { method: 'POST' });
      onRefresh();
    } catch (error) {
      console.error('Error toggling scraper:', error);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-6">
      <h2 className="text-xl font-semibold mb-4">Status</h2>
      <div className="flex items-center justify-between">
        <div>
          {isRunning ? (
            <span className="bg-green-500 text-white px-3 py-1 rounded-full text-sm">
              Running
            </span>
          ) : (
            <span className="bg-gray-500 text-white px-3 py-1 rounded-full text-sm">
              Stopped
            </span>
          )}
        </div>
        <button
          onClick={toggleScraper}
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md transition-colors"
        >
          {isRunning ? 'Stop' : 'Start'} Scraper
        </button>
      </div>
    </div>
  );
} 