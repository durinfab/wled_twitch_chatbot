import twitchio
from twitchio.ext import pubsub
from config import config

def startEventBot():
    print("starting event bot")
    my_token = config['STREAM']['Access_Token']
    client_sec = config['STREAM']['Client_Secret']
    users_oauth_token = config['STREAM']['Creator_Oauth']
    users_channel_id = int(config['STREAM']['Creator_Channel_ID'])
    client = twitchio.Client(token=my_token, client_secret=client_sec)
    client.pubsub = pubsub.PubSubPool(client)

    @client.event()
    async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
        print("Got bits event")
        pass # do stuff on bit redemptions

    @client.event()
    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        print("Got Channel Points")
        pass

    async def main():
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id]
        ]
        await client.pubsub.subscribe_topics(topics)
        await client.start()

    print("Start Event Looping")
    client.loop.run_until_complete(main())

