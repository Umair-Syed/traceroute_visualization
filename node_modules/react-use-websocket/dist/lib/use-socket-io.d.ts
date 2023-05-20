import { JsonValue, Options, WebSocketHook } from './types';
export interface SocketIOMessageData {
    type: string;
    payload: JsonValue | null;
}
export declare const useSocketIO: (url: string | (() => string | Promise<string>) | null, options?: Options, connect?: boolean) => WebSocketHook<SocketIOMessageData, SocketIOMessageData>;
