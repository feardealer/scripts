import asyncio
import websockets
import base64
import requests

async def captcha_client():
    uri = "ws://62.173.140.174:16011/ws"

    async with websockets.connect(uri) as websocket:
        await websocket.send("get_captcha")

        captcha_text = await websocket.recv()

        captcha_value = captcha_text.split(':')[-1].strip()

        decoded_captcha = base64.b64decode(captcha_value).decode('utf-8')

        operation = decoded_captcha.split('=')[-1].strip()

        try:
            result = eval(operation)
        except Exception as e:
            result = None
            print(f"Error during evaluation: {e}")

        print(f"{captcha_value} {decoded_captcha} = {result}")

        await websocket.send(str(result))
        response = await websocket.recv()

        print(f"Server Response: {response}")


# unfinished ;(

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(captcha_client())

