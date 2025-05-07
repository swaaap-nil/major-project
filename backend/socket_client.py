import asyncio
import threading
import socketio

from producer.rabbitmq import RabbitMQHelper
  # Import your helper class

# Initialize Socket.IO client
sio = socketio.AsyncClient()

# Initialize RabbitMQHelper
rabbitmq = RabbitMQHelper()

def process_message(message):
    """Callback function to process RabbitMQ messages and send via WebSockets"""
    print(f"[📩] Processing Message: {message}")

    # Emit event to frontend using thread-safe method
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run_coroutine_threadsafe(sio.emit("new_job", message), loop)

def start_rabbitmq():
    """Start RabbitMQ consumer in a background thread"""
    mq_thread = threading.Thread(target=rabbitmq.consume_messages, args=("notifications_queue", process_message), daemon=True)
    mq_thread.start()

# ✅ WebSocket Event Handling
@sio.event
async def connect():
    print("✅ WebSocket connected")
    await sio.emit("server_message", {"message": "Connected!"})

@sio.event
async def disconnect():
    print("❌ WebSocket disconnected")

# ✅ Main function
async def main():
    start_rabbitmq()  # Start RabbitMQ consumer in background
    await sio.connect("http://localhost:5000")
    await sio.wait()

if __name__ == "__main__":
    asyncio.run(main())
