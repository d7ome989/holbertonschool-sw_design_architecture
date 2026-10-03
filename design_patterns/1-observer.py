#!/usr/bin/env python3


class NewsSubject:
    def __init__(self):
        self._observers = {}

    def subscribe(self, observer, topics=None):
        self._observers[observer] = topics

    def unsubscribe(self, observer):
        self._observers.pop(observer, None)

    def notify(self, topic, data):
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()
    subject.subscribe(LogObserver(), topics={"sports", "breaking"})
    subject.subscribe(EmailObserver())
    subject.subscribe(SmsObserver(), topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


main()
