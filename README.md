# Akvelon Test task

## INTRO
This service was created by Flask and deployed to GCP. Cloud SQL (PostgreSQL) is used as a database. The service endpoint is implemented with Cloud Run, allowing flexible handling of the workload. And also we can migrate this POC to any platform (Kubernetes)

## Example of usage

Create new user:
```bash
curl -X POST  https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/create-user  -H "Content-Type: application/json" -d '{"first_name":"Vadim", "last_name":"Petrov", "email":"vadpetrov@mail.ru"}'
```
Result:
```bash
{"result":"Ok","user_id_new":15}
```
Getting information about user:
```bash
curl -X GET  https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/get-user/15
```
Result:
```bash
{"results":{"email":"vadpetrov@mail.ru","first_name":"Vadim","id":15,"last_name":"Petrov"}}
```
Update user's info:
```bash
curl -X POST  https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/update-user/1  -H "Content-Type: application/json" -d '{"last_name":"Sidorov"}'
```
Delete users info (Cascade delete transactions from table transaction):
```bash
curl -X POST  https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/delete-user/1
```
Insert user transaction:
```bash
curl -X POST https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/create-transaction/15 -H "Content-Type: application/json" -d '{"amount":"2100", "date":"2021-06-15 13:15:55"}'
curl -X POST https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/create-transaction/15 -H "Content-Type: application/json" -d '{"amount":"-100", "date":"2021-06-17 14:22:12"}'
```
Report by user:
```bash
curl -X GET https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/get-report/15
```
Result:
```bash
{"results":[{"date":"Tue, 15 Jun 2021 00:00:00 GMT","sum":2100.0},{"date":"Thu, 17 Jun 2021 00:00:00 GMT","sum":-100.0},{"date":"Sat, 19 Jun 2021 00:00:00 GMT","sum":100.0},{"date":"Sun, 20 Jun 2021 00:00:00 GMT","sum":-100.0}]}
```
Fibonacci function:
```bash
curl -X GET https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/fibonacci/7
curl -X GET https://test-akvelon-api-ehhdhtwuva-uw.a.run.app/fibonacci/0
```
Result:
```bash
{"result":13}
{"result":0}
```
