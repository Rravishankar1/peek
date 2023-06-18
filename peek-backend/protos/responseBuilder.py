from protos.peek_pb2 import (
    peekResponse,
    topic,
    notif
)

from compute.ml.hume_analysis import humeAnalysis

class responseBuilder:
    def __init__(self):
        self.response = peekResponse()

    def addTopic(self, name, highlight, summary, notifs):
        new_topic = self.response.topics.add()
        new_topic.name = name
        new_topic.emoji = humeAnalysis(summary)
        new_topic.highlight = highlight
        new_topic.summary = summary
        for notif in notifs:
            self._addNotif(new_topic, notif['title'], notif['uri'])
        return self

    def _addNotif(self, topic, title, uri):
        new_notif = topic.notifs.add()
        new_notif.title = title
        new_notif.uri = uri
        return self

    def build(self):
        print("Response built:\n" + str(self.response))
        return self.response
    
    def getTestResponse(self):
        return peekResponse(
            topics=[
                topic(
                    name="testTopic3",
                    emoji="123",
                    highlight="testHighlight",
                    summary="testSummary",
                    notifs=[
                        notif(
                            title="testTitle1",
                            uri="testURI1"
                        ),
                        notif(
                            title="testTitle2",
                            uri="testURI2"
                        )
                    ]
                ),
                topic(
                    name="testTopic2",
                    emoji="123",
                    highlight="testHighlight2",
                    summary="testSummary2",
                    notifs=[
                        notif(
                            title="testTitle3",
                            uri="testURI3"
                        ),
                        notif(
                            title="testTitle4",
                            uri="testURI4"
                        )
                    ]
                )
            ]
        )