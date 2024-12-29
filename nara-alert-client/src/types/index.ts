export interface SlackConfig {
  webhookUrl: string;
  channelName: string;
}

export interface SearchConfig {
  keyword: string;
  slackConfig: SlackConfig;
}
