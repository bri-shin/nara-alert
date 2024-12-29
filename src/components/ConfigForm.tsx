'use client';

import { useState } from 'react';
import { Config, Channel } from '@/types';

interface ConfigFormProps {
  initialConfig: Config;
  channels: Channel[];
  onConfigSaved: () => void;
}

export default function ConfigForm({ initialConfig, channels, onConfigSaved }: ConfigFormProps) {
  const [config, setConfig] = useState(initialConfig);
  const [saving, setSaving] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true);

    try {
      const response = await fetch('/api/config', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(config),
      });

      const data = await response.json();
      if (data.success) {
        alert('Settings saved successfully!');
        onConfigSaved();
      } else {
        alert(`Error: ${data.error}`);
      }
    } catch (error) {
      console.error('Error saving config:', error);
      alert('Error saving configuration');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold mb-4">Settings</h2>
      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Slack Bot Token
            </label>
            <input
              type="text"
              value={config.slack_token}
              onChange={(e) => setConfig({ ...config, slack_token: e.target.value })}
              className="w-full px-3 py-2 border rounded-md"
              required
              placeholder="xoxb-your-token"
            />
            <p className="text-sm text-gray-500 mt-1">
              Your Slack Bot Token (starts with xoxb-)
            </p>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Slack Channel
            </label>
            <select
              value={config.channel}
              onChange={(e) => setConfig({ ...config, channel: e.target.value })}
              className="w-full px-3 py-2 border rounded-md"
              required
            >
              {channels.map((channel) => (
                <option key={channel.id} value={`#${channel.name}`}>
                  #{channel.name}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Search Keyword
            </label>
            <input
              type="text"
              value={config.keyword}
              onChange={(e) => setConfig({ ...config, keyword: e.target.value })}
              className="w-full px-3 py-2 border rounded-md"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Check Interval (minutes)
            </label>
            <input
              type="number"
              value={config.check_interval}
              onChange={(e) => setConfig({ ...config, check_interval: parseInt(e.target.value) })}
              className="w-full px-3 py-2 border rounded-md"
              min="1"
              required
            />
          </div>

          <button
            type="submit"
            disabled={saving}
            className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md transition-colors disabled:opacity-50"
          >
            {saving ? 'Saving...' : 'Save Settings'}
          </button>
        </div>
      </form>
    </div>
  );
} 