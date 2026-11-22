# posted.base

Base module for the `posted` package.

This module contains the base class for message brokers, ‘MsgBrokerBase’, which defines
the interface for message brokers.

### Classes

| [`MsgBrokerBase`](#posted.base.MsgBrokerBase)(\*[, encoder, decoder])   | Base class for message brokers.   |
|------------------------------------------------------------------------------------------|-----------------------------------|

### *class* posted.base.MsgBrokerBase(, encoder=None, decoder=None, \*\*kwargs)

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for message brokers. Subclasses must implement the ‘write’, ‘read’,
‘subscribe’, and ‘unsubscribe’ methods.

#### read(channel)

Read a message from the channel.

* **Parameters:**
  **channel** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – The channel to read from.
* **Returns:**
  The message read from the channel.

#### subscribe(channel, callback)

Subscribe to a channel.

* **Parameters:**
  * **channel** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – The channel to subscribe to.
  * **callback** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], [`None`](https://docs.python.org/3/builtins/constants.html#None)]) – The callback to call when a message is received on the channel.

#### unsubscribe(channel)

Unsubscribe from a channel.

* **Parameters:**
  **channel** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – The channel to unsubscribe from.

#### write(channel, message)

Write a message to the channel.

* **Parameters:**
  * **channel** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – The channel to write to.
  * **message** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any)) – The message to write.
