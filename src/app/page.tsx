'use client';

import { useState, useEffect } from 'react';
import { Config, Channel } from '@/types';
import ConfigForm from '@/components/ConfigForm';
import StatusCard from '@/components/StatusCard';

export default function Home() {
  const [config, setConfig] = useState<Config | null>(null);
  const [channels, setChannels] = useState<Channel[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchConfig();
  }, []);

  const fetchConfig = async () => {
    try {
      const response = await fetch('/api/config');
      const data = await response.json();
      setConfig(data.config);
      setChannels(data.channels);
    } catch (error) {
      console.error('Error fetching config:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <main className="container mx-auto px-4 py-8 max-w-3xl">
      <h1 className="text-3xl font-bold mb-8">dain_scraper Configuration</h1>
      
      {config && (
        <>
          <StatusCard 
            isRunning={config.is_running} 
            onRefresh={fetchConfig} 
          />
          <ConfigForm 
            initialConfig={config}
            channels={channels}
            onConfigSaved={fetchConfig}
          />
        </>
      )}
    </main>
  );
} 