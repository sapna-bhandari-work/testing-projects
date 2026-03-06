# REST API Testing Suite — JSONPlaceholder

A dual-implementation REST API test suite that validates the public
[JSONPlaceholder](https://jsonplaceholder.typicode.com) mock API using two
parallel toolchains:

| Implementation | Files |
|---|---|
| **Postman** | `postman/JSONPlaceholder_Collection.json` + environment file |
| **Python / PyTest** | `python_suite/` — Requests library + jsonschema + pytest-html |

Both implementations cover identical test scenarios so teams can choose the tool
that fits their workflow (manual exploratory testing via Postman vs CI-integrated
automated runs via PyTest).

---

## Tech Stack

| Layer | Tool | Version | Purpose |
|---|---|---|---|
| HTTP client | [Requests](https://docs.python-requests.org/) | 2.31.0 | Python API calls |
| Test runner | [PyTest](https://pytest.org/) | 7.4.4 | Test discovery, execution, assertions |
| HTML reporting | [pytest-html](https://pytest-html.readthedocs.io/) | 4.1.1 | Self-contained HTML test report |
| Schema validation | [jsonschema](https://python-jsonschema.readthedocs.io/) | 4.21.1 | Draft-07 JSON Schema validation |
| API mocking | [JSONPlaceholder](https://jsonplaceholder.typicode.com) | public | Free REST mock API (posts, users) |
| GUI/Manual | [Postman](https://www.postman.com/) | Desktop v10+ | Collection runner, visual assertions |
| CI headless | [Newman](https://www.npmjs.com/package/newman) | latest | Postman CLI runner |

---

## Project Structure

```
api-testing-suite/
│
├── postman/                          # Postman implementation
│   ├── JSONPlaceholder_Collection.json   # v2.1 collection — all requests + test scripts
│   └── JSONPlaceholder_Environment.json  # Environment variables (base_url, post_id, user_id)
│
├── python_suite/                     # Python / PyTest implementation
│   │
│   ├── tests/                        # PyTest test modules
│   │   ├── __init__.py
│   │   ├── test_get.py               # GET /posts, GET /posts/1, GET /users/1, 404, filtering
│   │   ├── test_post.py              # POST /posts — valid payload, empty body, auto id
│   │   ├── test_put.py               # PUT /posts/1 — title update, id verification
│   │   └── test_delete.py            # DELETE /posts/1 and /posts/9999
│   │
│   ├── utils/                        # Shared helper modules
│   │   ├── __init__.py
│   │   ├── api_client.py             # Reusable ApiClient class wrapping requests.Session
│   │   └── schema_validator.py       # load_schema() + validate_schema() via jsonschema
│   │
│   ├── schemas/                      # JSON Schema Draft-07 definition files
│   │   ├── post_schema.json          # Schema for /posts resource objects
│   │   └── user_schema.json          # Schema for /users resource objects
│   │
│   ├── data/                         # Centralised test data
│   │   ├── __init__.py
│   │   └── payloads.py               # All request body dicts (never inline in tests)
│   │
│   ├── reports/                      # pytest-html output directory (auto-created)
│   │   └── .gitkeep
│   │
│   ├── conftest.py                   # Session-scoped ApiClient fixture
│   ├── requirements.txt              # Pinned Python dependencies
│   └── pytest.ini                    # Test paths, pythonpath, HTML report options, markers
│
└── README.md                         # This file
```

---

## Setup — Python Suite

### Prerequisites

- Python 3.9 or higher
- pip

### 1. Create and activate a virtual environment

```bash
# From the repository root
cd api-testing-suite/python_suite

python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the full test suite

```bash
# From python_suite/ with the venv active
pytest
```

The `pytest.ini` configuration automatically:
- discovers tests in `tests/`
- adds the project root to `sys.path`
- generates `reports/report.html`

### 4. Run a specific test file or test

```bash
# Single file
pytest tests/test_get.py

# Single test by name
pytest tests/test_get.py::TestGetSinglePost::test_schema_matches_post_schema

# All tests matching a keyword
pytest -k "schema"

# Verbose output without HTML report
pytest -v --no-header -p no:html
```

### 5. Override the base URL

```bash
API_BASE_URL=http://localhost:3000 pytest
```

### 6. View the HTML report

After a run, open the self-contained report file in any browser:

```
python_suite/reports/report.html
```

---

## Setup — Postman Collection

### Option A: Postman Desktop

1. Open **Postman Desktop** (v10 or later recommended).
2. Click **Import** (top-left).
3. Drag-and-drop both files, or use **Upload Files**:
   - `postman/JSONPlaceholder_Collection.json`
   - `postman/JSONPlaceholder_Environment.json`
4. Select the **JSONPlaceholder Environment** from the environment dropdown
   (top-right of the workspace).
5. Open the **JSONPlaceholder API Test Suite** collection and click **Run collection**.

### Option B: Newman CLI (CI/CD)

Newman runs the collection headlessly and is suitable for pipelines (GitHub
Actions, GitLab CI, Jenkins, etc.).

```bash
# Install Newman globally
npm install -g newman

# Install the HTML extra reporter (optional but recommended)
npm install -g newman-reporter-htmlextra

# Run with the bundled environment file
newman run postman/JSONPlaceholder_Collection.json \
    --environment postman/JSONPlaceholder_Environment.json \
    --reporters cli,htmlextra \
    --reporter-htmlextra-export newman-report.html

# Exit code is non-zero on any test failure — safe for CI gating
```

**Minimum Newman run (no extras):**

```bash
newman run postman/JSONPlaceholder_Collection.json \
    --environment postman/JSONPlaceholder_Environment.json
```

---

## Test Coverage Matrix

| Endpoint | Method | Scenario | Tool(s) | Expected Status |
|---|---|---|---|---|
| `/posts` | GET | Returns 200 | Python, Postman | 200 |
| `/posts` | GET | Response is a list | Python, Postman | 200 |
| `/posts` | GET | List is non-empty | Python, Postman | 200 |
| `/posts` | GET | Response time < 2 000 ms | Python, Postman | 200 |
| `/posts/1` | GET | Returns 200 | Python, Postman | 200 |
| `/posts/1` | GET | Required keys: id, title, body, userId | Python, Postman | 200 |
| `/posts/1` | GET | Response matches `post_schema.json` (Draft-07) | Python, Postman | 200 |
| `/posts/1` | GET | Response time < 2 000 ms | Python, Postman | 200 |
| `/posts/9999` | GET | Non-existent resource returns 404 | Python, Postman | 404 |
| `/posts?userId=1` | GET | Returns 200 | Python, Postman | 200 |
| `/posts?userId=1` | GET | All items have `userId == 1` | Python, Postman | 200 |
| `/users/1` | GET | Returns 200 | Python, Postman | 200 |
| `/users/1` | GET | Response matches `user_schema.json` (Draft-07) | Python, Postman | 200 |
| `/users/1` | GET | Response time < 2 000 ms | Python, Postman | 200 |
| `/posts` | POST | Valid payload returns 201 | Python, Postman | 201 |
| `/posts` | POST | Response echoes title, body, userId | Python, Postman | 201 |
| `/posts` | POST | Response contains auto-generated integer `id` | Python, Postman | 201 |
| `/posts` | POST | Empty body returns 201 *(mock limitation)* | Python, Postman | 201 |
| `/posts` | POST | Response time < 2 000 ms | Python, Postman | 201 |
| `/posts/1` | PUT | Returns 200 | Python, Postman | 200 |
| `/posts/1` | PUT | Response `title` matches sent value | Python, Postman | 200 |
| `/posts/1` | PUT | Response `id` equals route parameter (1) | Python, Postman | 200 |
| `/posts/1` | PUT | Response time < 2 000 ms | Python, Postman | 200 |
| `/posts/1` | DELETE | Returns 200 | Python, Postman | 200 |
| `/posts/1` | DELETE | Response body is `{}` | Python, Postman | 200 |
| `/posts/9999` | DELETE | Returns 200 *(mock limitation)* | Python, Postman | 200 |
| `/posts/1` | DELETE | Response time < 2 000 ms | Python, Postman | 200 |

**Total: 27 discrete test assertions across 4 HTTP methods and 5 endpoints.**

---

## JSONPlaceholder API Limitations

JSONPlaceholder is a free, read-only mock API intended for prototyping and
learning. Be aware of the following constraints when interpreting test results:

| Limitation | Detail |
|---|---|
| **No data persistence** | POST, PUT, and DELETE calls appear to succeed but no changes are stored. A subsequent GET returns the original seed data. |
| **No input validation** | The API accepts any payload including empty or malformed bodies and returns 201/200. Production APIs should reject invalid input with 400/422. |
| **DELETE always 200** | DELETE returns HTTP 200 even for resource IDs that do not exist (e.g., `/posts/9999`). Production APIs should return 404 for non-existent resources. |
| **Fixed id on POST** | POST /posts always returns `id: 101` regardless of how many resources have been "created". This is a simulation, not a real auto-increment. |
| **Rate limiting** | No authentication required, but abusive usage may be throttled. The test suite makes one request per test — this is well within limits. |
| **HTTPS only** | The API enforces HTTPS. HTTP requests are not accepted. |

---

## Author

<!-- Replace with your name and contact details -->
**Author:** _Your Name_
**Contact:** _your.email@example.com_
**Date:** March 2026
