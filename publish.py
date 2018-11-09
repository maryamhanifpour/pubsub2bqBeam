from google.cloud import pubsub
import json
import datetime

ts_init = datetime.datetime.now()
ts_init_str = ts_init.strftime("%Y-%m-%d %H:%M:%S")
publisher = pubsub.PublisherClient()
topic_name = ''

def trigger(request):
    ts_event = datetime.datetime.now()
    ts_event_str = ts_event.strftime("%Y-%m-%d %H:%M:%S")

    data = dict()
    with open('msg.json') as f:
        data = json.load(f)

    data["ts_event"] = ts_event_str
    event_str = json.dumps(data)
    print(event_str.encode('utf-8'))
    publisher.publish(topic_name, event_str.encode('utf-8'), atag='avalue')

trigger(None)