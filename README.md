
### For Backend

What things you need to install the software and how to install them

```
$ pip install -r requirements.txt
```
Also setup mysql server

### To Run


Say what the step will be

```
$ python3 run.py
```

### Assumptions

The APIs can be more modular and can be linked with the middleware in case of video upload

Recommendation API can be discussed in detail based on the logs data

The complete code can be divided into follwing pattern

```
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
```
> Can discuss for microservices, design patterns and system design for code scalability