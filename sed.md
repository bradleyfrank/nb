# sed

Parsing between patterns:

```text
---
foo: bar
bat: baz
---
Suspendisse sed sodales ipsum. Nam hendrerit velit eu orci commodo, quis ultricies lectus egestas.
```

* Text between pattern: `sed -n '/---/,/---/p' FILE`
* Text outside pattern: `sed '/---/,/---/d' FILE
