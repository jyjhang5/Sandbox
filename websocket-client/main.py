import websocket

def on_message(ws, message):
    print(f"Received message: {message}")
    # binary_representation = ' '.join(format(byte, '08b') for byte in message)
    # print(f"Binary representation: {binary_representation}")

    hex_representation = ' '.join(hex(byte) for byte in message)
    print(f"Hex: {hex_representation}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Closed with status code {close_status_code}: {close_msg}")

def on_open(ws):
    print("Connected to the WebSocket")
    
    # Send a sample message after connection
    ws.send("Hello, WebSocket!")

if __name__ == "__main__":
    # Replace the URL with your WebSocket server URL
    ws_url = "ws://10.100.105.119/wsbackend"
    # ws_url = "ws://10.100.105.114/wsbackend"

    # Create a WebSocket instance and set the event handlers
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open

    # Start the WebSocket connection
    ws.run_forever()
