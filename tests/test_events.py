from src.event_producer import EventProducer
from src.event_topic import EventTopic


def test_event_topic_starts_empty():
    topic = EventTopic("anomalies")

    assert topic.name == "anomalies"
    assert topic.get_messages() == []


def test_event_topic_publishes_messages():
    topic = EventTopic("anomalies")
    event = {"id": 1, "type": "anomaly"}

    topic.publish(event)

    assert topic.get_messages() == [event]


def test_get_messages_returns_a_copy():
    topic = EventTopic("anomalies")
    topic.publish({"id": 1})

    messages = topic.get_messages()
    messages.append({"id": 2})

    assert topic.get_messages() == [{"id": 1}]


def test_clear_removes_all_messages():
    topic = EventTopic("anomalies")
    topic.publish({"id": 1})

    topic.clear()

    assert topic.get_messages() == []


def test_producer_rejects_empty_event():
    topic = EventTopic("anomalies")
    producer = EventProducer(topic)

    assert producer.publish(None) is False
    assert producer.publish({}) is False
    assert topic.get_messages() == []


def test_producer_publishes_valid_event():
    topic = EventTopic("anomalies")
    producer = EventProducer(topic)
    event = {"id": 1, "severity": "high"}

    assert producer.publish(event) is True
    assert topic.get_messages() == [event]
