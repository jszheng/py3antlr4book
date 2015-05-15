# What's New
- Label multiple alternative with the same name and process with same function.

# How to Run
```
% type t.json
{
    "description" : "An imaginary server config file",
    "logs" : {"level":"verbose", "dir":"/var/log"},
    "host" : "antlr.org",
    "admin": ["parrt", "tombu"],
    "aliases": []
}

% python json2xml.py t.json

<description>An imaginary server config file</description>
<logs>
<level>verbose</level>
<dir>/var/log</dir>
</logs>
<host>antlr.org</host>
<admin>
<element>parrt</element>
<element>tombu</element>
</admin>
<aliases></aliases>

```