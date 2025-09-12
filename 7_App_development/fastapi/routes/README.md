
If you only use POST or GET for everything, several problems can occur:


- GET requests usually don’t have a body (and many clients/servers ignore it).

- Hard to send complex data for creating/updating resources.

- It breaks HTTP standards.

- Clients (mobile apps, browsers, proxies, gateways) may behave unexpectedly.

- It becomes harder to scale, secure, and integrate with modern tools.