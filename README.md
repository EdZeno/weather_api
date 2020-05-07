Weather service
===============

This is the test for backend developers.

Introduction
------------

Write an HTTP service which provides an API to get a weather
forecast for a given city.

I will use the [openweathermap](https://www.openweathermap.org) API as
the data source. The API requires an API key that can be obtained for free
after [signing up](https://home.openweathermap.org/users/sign_up)

Getting it running
------------------

The Service
-----------

The user can make the following calls against this web service using
[curl](https://curl.haxx.se/)

### `/ping`

This is a simple health check that we can use to determine that the service is
running, and provides information about the application. The `"version"`
attribute in the response should match the version number in the `VERSION`
file.

```bash
$ curl -si http://localhost:8080/ping

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
  "name": "weatherservice",
  "status": "ok",
  "version": "1.0.0"
}
```

### `/forecast/<city>`

This endpoint allows a user to request a breakdown of the current weather for
a specific city. The response should include a description of the cloud cover,
the humidity as a percentage, the pressure in hecto Pascals (hPa), and
temperature in Celsius.

Cloud coverage should use the following scale:

| cloud coverage | description      |
|----------------|------------------|
| 0-10%          | clear sky        |
| 10-36%         | few clouds       |
| 37-60%         | scattered clouds |
| 61-84%         | broken clouds    |
| 85-100%        | overcast         |

For example fetching the weather data for London should look like this:

```bash
$ curl -si http://localhost:8080/forecast/london/

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
    "clouds": "broken clouds",
    "humidity": "66.6%",
    "pressure": "1027.51 hPa",
    "temperature": "14.4C"
}
```

### Errors

When no data is found or the endpoint is invalid the service should respond
with `404` status code and an appropriate message:

```bash
$ curl -si http://localhost:8080/forecast/westeros

HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8
{
    "error": "Cannot find country 'westeros'",
    "error_code": "country not found"
}
```

Similarly invalid requests should return a `400` status code:

```bash
$ curl -si http://localhost:8080/forecast

HTTP/1.1 400 Bad Request
Content-Type: application/json; charset=utf-8
{
    "error": "no city provided",
    "error_code": "invalid request"
}
```

If anything else goes wrong the service should response with a `500` status code
and a message that doesn't leak any information about the service internals:

```bash
$ curl -si http://localhost:8080/forecast/london

HTTP/1.1 500 Internal Server Error
Content-Type: application/json; charset=utf-8
{
    "error": "Something went wrong",
    "error_code": "internal server error"
}
```
