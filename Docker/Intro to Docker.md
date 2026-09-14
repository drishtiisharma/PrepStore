# Introduction to Docker

## What Problem Did Docker Solve?

Before Docker, developers faced these issues:
- **"It works on my machine"**: Code worked in development but failed in production due to different environments
- **Dependency conflicts**: Different applications needed different versions of the same library
- **Complex setup**: Installing and configuring software took hours or days
- **Inconsistent environments**: Development, testing, and production had different configurations

Docker solved this by packaging applications with everything they need (code, runtime, libraries, system tools) into standardized units called containers.

## Core Concepts

### 1. **Image**
- A read-only template that contains instructions for creating a container
- Built from a Dockerfile
- Stored in layers (each instruction creates a new layer)
- Can be shared via registries (like Docker Hub)

### 2. **Container**
- A running instance of an image
- Isolated process with its own filesystem, networking, and resources
- Lightweight because it shares the host OS kernel
- Can be started, stopped, deleted easily

### 3. **Dockerfile**
- A text file with instructions to build an image
- Each instruction creates a layer in the image
- Example:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 4. **Docker Hub/Registry**
- Centralized storage for Docker images
- Docker Hub is the default public registry
- You can push/pull images from here

### 5. **Volume**
- Persistent storage that survives container deletion
- Maps a directory on the host to a directory in the container
- Used for databases, logs, configuration files

### 6. **Network**
- Allows containers to communicate
- Types: bridge (default), host, none, custom networks
- Containers can discover each other by name

### 7. **Docker Compose**
- Tool for defining multi-container applications
- Uses YAML file to configure services
- Manages multiple containers as one application

## Key Terminologies

| Term | Definition |
|------|------------|
| **Daemon** | Background service that manages containers |
| **Client** | Command-line tool that communicates with daemon |
| **Layer** | Read-only filesystem changes from Dockerfile instructions |
| **Tag** | Label for image versions (e.g., latest, 1.0, stable) |
| **Build Context** | Directory sent to Docker daemon during build |
| **Entrypoint** | Primary command that runs when container starts |
| **CMD** | Default arguments for entrypoint or primary command |

## Essential Commands

### Image Management
```bash
# Build an image from Dockerfile
docker build -t myapp:1.0 .

# List images
docker images

# Pull image from registry
docker pull nginx:latest

# Remove image
docker rmi myapp:1.0
```

### Container Management
```bash
# Run a container
docker run -d -p 8080:80 --name mycontainer myapp:1.0

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop mycontainer

# Start a stopped container
docker start mycontainer

# Remove a container
docker rm mycontainer

# View container logs
docker logs mycontainer

# Execute command in running container
docker exec -it mycontainer bash
```

### Common Flags
- `-d`: Detached mode (run in background)
- `-p host_port:container_port`: Port mapping
- `--name`: Assign a name to container
- `-v host_path:container_path`: Volume mount
- `-e KEY=value`: Set environment variable
- `--rm`: Auto-remove container when it stops
- `-it`: Interactive mode with terminal

## How Docker Works Internally

1. **Namespaces**: Provide isolation (PID, network, mount, user, IPC, UTS)
2. **Control Groups (cgroups)**: Limit resource usage (CPU, memory, I/O)
3. **Union Filesystem**: Layered filesystem for images (OverlayFS, AUFS)
4. **Container Runtime**: Actually runs containers (containerd, runc)

## Docker vs Virtual Machines

| Aspect | Docker | VM |
|--------|--------|-----|
| **OS** | Shares host kernel | Full guest OS |
| **Size** | MBs | GBs |
| **Boot Time** | Seconds | Minutes |
| **Performance** | Near-native | Overhead from hypervisor |
| **Isolation** | Process-level | Hardware-level |
| **Use Case** | Microservices, apps | Legacy apps, different OS |

## Best Practices for Production

1. **Use specific tags**, not "latest"
2. **Minimize layers** by combining RUN commands
3. **Use .dockerignore** to exclude unnecessary files
4. **Run as non-root user** for security
5. **Use multi-stage builds** to reduce image size
6. **Keep secrets out of images** (use environment variables or secret management)
7. **Health checks** to monitor container status
8. **Resource limits** to prevent resource exhaustion

Example of multi-stage build:
```dockerfile
# Build stage
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

## Interview Questions to Prepare

### Basic Level
1. What is Docker and why use it?
2. Difference between image and container?
3. What is a Dockerfile?
4. How do you create and run a container?
5. What is Docker Hub?

### Intermediate Level
1. Explain Docker architecture
2. What are volumes and why use them?
3. How does Docker networking work?
4. What is Docker Compose?
5. How to optimize Docker image size?
6. Difference between CMD and ENTRYPOINT?
7. How to pass environment variables?

### Advanced Level
1. How does Docker achieve isolation?
2. Explain multi-stage builds
3. How to secure Docker containers?
4. What is container orchestration? (Kubernetes)
5. How to debug a failing container?
6. Explain Docker layer caching
7. What are health checks?

## Practical Exercise

Create a simple Python Flask app with Docker:

**app.py:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt:**
```
flask==2.0.1
```

**Dockerfile:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Build and run:**
```bash
docker build -t flask-app .
docker run -d -p 5000:5000 --name myflask flask-app
```

## Study Tips for You

Since you're a coder who prefers digital notes:
1. **Create a cheat sheet** with common commands
2. **Practice building images** from scratch
3. **Experiment with Docker Compose** for multi-service apps
4. **Read official documentation** at docs.docker.com
5. **Try breaking things** and learn to debug
6. **Set up a personal project** with Docker to gain hands-on experience

Would you like me to dive deeper into any specific topic, such as Docker Compose, networking, or advanced optimization techniques?