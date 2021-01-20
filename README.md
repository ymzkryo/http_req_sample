# dependency

```
pip install -r requirements.txt
```

# Using

```
python main.py
```

## get

```
curl localhost:8000
```

result:  

```json
{"mgs":"failure"}
```

## post

```
curl -XPOST -d '{ "hoge" : 1, "bar" : "bar" }' http://localhost:8000
```

result:  
```json
{"status": 200, "result": {"hoge": 100, "bar": "bar"}}
```
