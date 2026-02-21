# Blood Bank Management System

A Dockerized Django + MySQL application.

---

## 🚀 Requirements

Make sure you have installed:

- Docker
- Docker Compose (v2 → `docker compose`)

Check versions:

```bash
docker --version
docker compose version
```

---

## 📁 Project Structure

```
bloodbankmanagementsystem/
│
├── docker-compose.yml
├── Dockerfile
├── webapp/
├── database/
│   └── bbdmspythondb.sql
└── README.md
```

---

## 🟢 Start the Application

From the project root directory:

```bash
docker compose up --build
```

What this does:

- Builds Django image
- Starts MySQL container
- Waits for DB to be ready
- Runs migrations
- Starts Django server

---

### 🌐 Access the App

Open browser:

`http://localhost:8000`

---

## 🛑 Stop the Application

Press:

```bash
CTRL + C
```

Then run:

```bash
docker compose down
```

This stops and removes containers
⚠️ Database data will be preserved (volume remains).

---

## 🔄 Stop and Remove Everything (Including Database)

If you want a completely fresh start:

```bash
docker compose down -v
```

This removes:

- Containers
- Network
- Database volume

Next time you run `docker compose up`, the database will be recreated and the `.sql` file will run again.

---

## 🔁 Run in Detached Mode (Background)

Start containers in background:

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Stop background containers:

```bash
docker compose down
```

---

## 🧹 Rebuild After Code Changes

If you modify:

- `Dockerfile`
- `requirements.txt`

Run:

```bash
docker compose up --build
```

If only Django code changed:

```bash
docker compose restart
```

---

## 🛠 Database Access (Optional)

To enter MySQL container:

```bash
docker compose exec db mysql -u root -p
```

Enter the root password when prompted.

---

## 🐛 Common Issues

### ❌ Port already in use

If you see:

```log
Port 8000 is already allocated
```

Stop other services using that port or change it in `docker-compose.yml`.

---

### ❌ Database not connecting

Make sure in Django settings:

```python
'HOST': 'db'
```

NOT `localhost`.

---

## 📌 Useful Commands Summary

| Action              | Command                     |
| ------------------- | --------------------------- |
| Start app           | `docker compose up --build` |
| Start in background | `docker compose up -d`      |
| Stop app            | `docker compose down`       |
| Remove DB data      | `docker compose down -v`    |
| View logs           | `docker compose logs -f`    |
