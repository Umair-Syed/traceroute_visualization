import { Options, WebSocketHook, JsonValue } from './types';
export declare const useWebSocket: <T extends JsonValue | null = JsonValue | null>(url: string | (() => string | Promise<string>) | null, options?: Options, connect?: boolean) => WebSocketHook<T, MessageEvent<any> | null>;
