'use client';

import { useState } from 'react';
import { SearchConfig } from '@/types';

export default function Home() {
  const [config, setConfig] = useState<SearchConfig>({
    keyword: '',
    slackConfig: {
      webhookUrl: '',
      channelName: '',
    },
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/configure', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(config),
      });
      
      if (response.ok) {
        alert('Configuration saved successfully!');
      } else {
        throw new Error('Failed to save configuration');
      }
    } catch (error) {
      alert('Error saving configuration');
      console.error(error);
    }
  };

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-8">Nara Alert Configuration</h1>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-4">
            <h2 className="text-xl font-semibold">Search Settings</h2>
            <div>
              <label htmlFor="keyword" className="block text-sm font-medium mb-1">
                Search Keyword
              </label>
              <input
                type="text"
                id="keyword"
                value={config.keyword}
                onChange={(e) => setConfig({ ...config, keyword: e.target.value })}
                className="w-full p-2 border rounded-md"
                required
              />
            </div>
          </div>

          <div className="space-y-4">
            <h2 className="text-xl font-semibold">Slack Integration</h2>
            <div>
              <label htmlFor="webhookUrl" className="block text-sm font-medium mb-1">
                Slack Webhook URL
              </label>
              <input
                type="url"
                id="webhookUrl"
                value={config.slackConfig.webhookUrl}
                onChange={(e) =>
                  setConfig({
                    ...config,
                    slackConfig: { ...config.slackConfig, webhookUrl: e.target.value },
                  })
                }
                className="w-full p-2 border rounded-md"
                required
              />
            </div>
            <div>
              <label htmlFor="channelName" className="block text-sm font-medium mb-1">
                Slack Channel Name
              </label>
              <input
                type="text"
                id="channelName"
                value={config.slackConfig.channelName}
                onChange={(e) =>
                  setConfig({
                    ...config,
                    slackConfig: { ...config.slackConfig, channelName: e.target.value },
                  })
                }
                className="w-full p-2 border rounded-md"
                required
              />
            </div>
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition-colors"
          >
            Save Configuration
          </button>
        </form>
      </div>
    </main>
  );
}
