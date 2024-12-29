import { NextResponse } from 'next/server';
import type { SearchConfig } from '@/types';

export async function POST(request: Request) {
  try {
    const config: SearchConfig = await request.json();
    
    // Log the config to show it's being used
    console.log('Received configuration:', config);
    
    // TODO: Implement actual configuration storage
    return NextResponse.json({ 
      success: true,
      savedConfig: config  // Echo back the received config
    });
  } catch (error) {
    console.error('Configuration error:', error);
    return NextResponse.json(
      { error: 'Failed to save configuration' },
      { status: 500 }
    );
  }
}