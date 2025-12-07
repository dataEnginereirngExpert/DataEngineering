## REST API Basics

A **REST API** allows applications to communicate over the web.  
You send a **request**, and the server returns a **response** (usually in JSON format).

An API (Application Programming Interface) is a defined set of rules that allows different software components or systems to communicate with each other. It abstracts internal implementation and exposes only the required functionalities.

### Types of API Requests

- **GET** → Fetch data (most common)  
- **POST** → Create new data  
- **PUT/PATCH** → Update existing data  
- **DELETE** → Remove data  

For **data ingestion**, we mainly use the **GET** method.


# Commonly Used HTTP Status Codes

## 🟩 2xx — Success
| Code | Meaning |
|------|---------|
| **200 OK** | Request succeeded. |
| **201 Created** | Resource successfully created. |
| **202 Accepted** | Request accepted but processing not completed. |
| **204 No Content** | Success with no response body. |

---

## 🟦 3xx — Redirection
| Code | Meaning |
|------|---------|
| **301 Moved Permanently** | Resource permanently moved to new URL. |
| **302 Found** | Temporary redirect. |
| **304 Not Modified** | Use cached version; no need to re-download. |

---

## 🟧 4xx — Client Errors
| Code | Meaning |
|------|---------|
| **400 Bad Request** | Invalid request syntax or parameters. |
| **401 Unauthorized** | Authentication required or invalid token. |
| **403 Forbidden** | Authenticated but not allowed to access resource. |
| **404 Not Found** | Resource not found. |
| **405 Method Not Allowed** | Wrong HTTP method used. |
| **408 Request Timeout** | Client request took too long. |
| **429 Too Many Requests** | Rate limit exceeded. |

---

## 🟥 5xx — Server Errors
| Code | Meaning |
|------|---------|
| **500 Internal Server Error** | General server-side error. |
| **501 Not Implemented** | API endpoint not supported. |
| **502 Bad Gateway** | Invalid response from upstream server. |
| **503 Service Unavailable** | Server overwhelmed or down. |
| **504 Gateway Timeout** | Upstream server took too long to respond. |

To work with APIs in python , intsall **requests** library  **pip install requests**
Verify installation : **pip show requests**


## Authentication (API Key)
api_key = "YOUR_API_KEY"
url = f"https://api.example.com/data?apikey={api_key}"

response = requests.get(url)
OR
headers = {"Authorization": f"Bearer {api_key}"}

## Testing URL : https://fake-json-api.mock.beeceptor.com/users



