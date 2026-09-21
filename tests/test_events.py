from src.event_producer import EventProducer
from src.event_topic import EventTopic


def test_publish_valid_event():
    topic = EventTopic("anomalies")
    producer = EventProducer(topic)

    assert producer.publish({"id": 1}) is True
    assert topic.get_messages() == [{"id": 1}]


def test_publish_empty_event_is_ignored():
    topic = EventTopic("anomalies")
    producer = EventProducer(topic)

    assert producer.publish(None) is False
    assert topic.get_messages() == []


def test_topic_clear_removes_messages():
    topic = EventTopic("anomalies")
    topic.publish({"id": 1})

    topic.clear()

    assert topic.get_messages() == []
