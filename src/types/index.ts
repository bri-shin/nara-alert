export interface Config {
  slack_token: string;
  channel: string;
  keyword: string;
  check_interval: number;
  is_running: boolean;
}

export interface Channel {
  name: string;
  id: string;
} 