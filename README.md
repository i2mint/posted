
# posted
Interfacing with message-broker functionality


To install:	```pip install posted```


# Examples

`posted` defines the interface that message-broker backends implement: `MsgBrokerBase`, with `write`, `read`, `subscribe` and `unsubscribe`, plus the `NoMsg` sentinel for "nothing to read". Messages go through an `encoder` and `decoder` (JSON bytes by default), and the base class keeps the `_subscriptions` dict and a thread-pool `_executor` for subclasses to use.

Here is a minimal in-memory implementation, to show what a subclass has to provide (a real backend talks to a broker; [redisposted](https://github.com/i2mint/redisposted) is the Redis one):

```python
>>> from posted import MsgBrokerBase, NoMsg
>>>
>>> class InMemoryBroker(MsgBrokerBase):
...     def __init__(self, **kwargs):
...         super().__init__(**kwargs)
...         self._channels = {}
...     def write(self, channel, message):
...         data = self._encoder(message)
...         self._channels.setdefault(channel, []).append(data)
...         if channel in self._subscriptions:
...             self._subscriptions[channel](self._decoder(data))
...     def read(self, channel):
...         queue = self._channels.get(channel)
...         return self._decoder(queue.pop(0)) if queue else NoMsg
...     def subscribe(self, channel, callback):
...         self._subscriptions[channel] = callback
...     def unsubscribe(self, channel):
...         self._subscriptions.pop(channel, None)
>>>
>>> broker = InMemoryBroker()
>>> broker.write('greetings', {'hello': 'world'})
>>> broker.read('greetings')
{'hello': 'world'}
>>> broker.read('greetings') is NoMsg
True
>>> received = []
>>> broker.subscribe('news', received.append)
>>> broker.write('news', [1, 2, 3])
>>> received
[[1, 2, 3]]
```
