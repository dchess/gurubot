import os
import random
from slack import RTMClient


@RTMClient.run_on(event="message")
def say_hello(**payload):
    data = payload["data"]
    web_client = payload["web_client"]

    responses = [
        "https://www.youtube.com/watch?v=inpok4MKVLM",
        "https://youtu.be/LkoOCw_tp1I",
        "https://i.imgur.com/X6GIets.jpg",
        "https://i.imgur.com/sWpEsgs.jpg",
        "https://i.imgur.com/qhXFD4g.gif",
        "https://asoftmurmur.com/",
        "https://www.youtube.com/watch?v=kd7KC3PaEaA",
        "https://i.imgur.com/q32QBbf.mp4",
        "https://i.imgur.com/IiTD3m8.jpg",
        "https://i.imgur.com/hTZLKV7.gif",
        "https://i.imgur.com/6RtPDsO.jpg",
        "https://i.imgur.com/2bgYil3.mp4",
        "https://i.imgur.com/7qJwc4F.jpg",
        "https://i.imgur.com/nguENPl.jpg",
        "https://i.imgur.com/g0Zks3d.gif",
        "https://i.imgur.com/Yx4L4M4.jpg",
        "https://i.imgur.com/0sI8Ljx.jpg",
        "https://www.youtube.com/watch?v=ZVA-Bx4rNc0",
        "https://media.giphy.com/media/MJcARpb38uxxe/giphy.gif",
        "https://media3.giphy.com/media/neZ3NgNCKGxXy/giphy.gif",
    ]

    if "relax" in data.get("text"):
        channel_id = data["channel"]
        web_client.chat_postMessage(
            channel=channel_id, text=random.choice(responses)
        )
    else:
        channel_id = data["channel"]
        web_client.chat_postMessage(
            channel=channel_id, text="Not sure what you mean. Try *relax*.")
        )


if __name__ == "__main__":
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    rtm_client = RTMClient(token=slack_token)
    rtm_client.start()
