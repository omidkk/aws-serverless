# aws-serverless

Requirement:

```
Python > 3.8
```

Install:

Create virtual environment, and run:

```
pip install -r requirments 
```

Run:

```
cd app
uvicorn main:app --reload
```

Run Tests:

```
pytest app/tests/test_main.py
```

Swagger Link:

```
https://uit82n78x8.execute-api.eu-central-1.amazonaws.com/dev/docs
```

There are two endpoints, each uses different algorithm to resolve the challenge.

Repository has a GitHub Actions CI/CD integration. Each push triggers the CI/CD and deploys the code to the AWS.

Pre-Commit could be also added to the github actions to check format the code, and lint check.
