# 🚀 FastAPI Example App

This is a basic FastAPI project that demonstrates how to set up simple GET routes using FastAPI.

---

## 📖 What It Does

- Serves a **welcome message** at the root path `/`.
- Handles **dynamic URL routing** with path parameters.
- Accepts **optional query parameters** to make API calls more flexible.

---

## 🛠 Features

- ✅ Clean and simple API structure.
- 🔢 Supports dynamic URL segments (e.g., `/routes/2`).
- ❓ Accepts optional query parameters like `/routes/5?q=test`.
- ⚡ Fast development with automatic API documentation via Swagger.

---

## 🚀 How It Works

1. **Root Path `/`**: When you visit `/`, the server returns a welcome message.
2. **Dynamic Route `/routes/{route_id}`**: When you visit `/routes/{route_id}`, the server returns the value of `route_id`.
3. **Query Parameters**: You can pass a query string like `?q=something` to see it included in the response.

---

## 🧪 API Examples

- `GET /`  
  Response:  
  ```json
  { "HELLO": "WORLD" }
````

* `GET /routes/2`
  Response:

  ```json
  { "route_id": 2, "q": null }
  ```

* `GET /routes/5?q=hi`
  Response:

  ```json
  { "route_id": 5, "q": "hi" }
  ```

---

## 🖥️ How to Run the Server

1. Ensure you're in the project folder and have activated your virtual environment.

2. Run the development server using the following command:

   ```bash
   fastapi dev main.py
   ```

3. Open your browser and visit the following URLs:

   * [http://localhost:8000](http://localhost:8000) → Shows `{ "HELLO": "WORLD" }`
   * [http://localhost:8000/routes/2](http://localhost:8000/routes/2) → Shows `{ "route_id": 2, "q": null }`
   * [http://localhost:8000/routes/5?q=hi](http://localhost:8000/routes/5?q=hi) → Shows `{ "route_id": 5, "q": "hi" }`

---

## 🧰 Tools Used

* **FastAPI** — for building the API.
* **FastAPI CLI (`fastapi dev`)** — to run the app in development mode.
* **Uvicorn** — serves the app internally when using FastAPI CLI.

---

## 📌 Notes

Once the server is running, you can access the following:

* **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

```


