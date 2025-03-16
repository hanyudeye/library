
## 端口映射

Docker 端口映射是一种将容器内部的端口映射到主机上的特定端口的机制。这样可以使得容器内运行的服务可以通过主机的特定端口对外提供访问，从而实现容器与外部网络的通信。

要进行端口映射，可以使用 Docker 命令行工具或 Docker Compose 文件中的端口映射配置。下面是一些常用的方法：

### 使用 Docker 命令行工具
```bash
docker run -p 主机端口:容器端口 image_name
```
这条命令会将容器内部的 `容器端口` 映射到主机上的 `主机端口`，这样就可以通过主机的 `主机端口` 访问容器内的服务。

### 使用 Docker Compose 文件
在 Docker Compose 文件中，可以使用 `ports` 关键字来进行端口映射配置。示例：
```yaml
services:
  my_service:
    image: image_name
    ports:
      - "主机端口:容器端口"
```
这样配置后，使用 `docker-compose up` 启动容器时，端口映射就会生效。

### 多个端口映射
如果需要映射多个端口，可以在命令行工具或 Docker Compose 文件中使用多个 `-p` 参数或多个端口映射配置。

### 动态端口映射
有时候，也可以使用动态端口映射，让 Docker 自动选择一个未被占用的主机端口进行映射，例如：
```bash
docker run -p 容器端口 image_name
```

端口映射在 Docker 中是非常常见且重要的操作，它使得容器内的服务可以通过主机的端口与外部进行通信，提供了更加灵活和便捷的容器化应用部署方式。


## 提交容器副本使之成为一个新的镜像

docker commit -m="提交的描述信息" -a="作者" 容器ID 要创建的目标镜像名:[标签名]

### 运行 Linux 容器

#### 启动 Ubuntu 容器：
```bash
docker run -it ubuntu
```

这个命令会：
- 启动一个新的 Ubuntu 容器。
- 使用 `-it` 参数启动容器，并分配一个伪终端（Interactive Terminal），让你能够进入容器进行操作。

如果你拉取的是 **Debian** 或 **Alpine**，只需要将镜像名称替换为相应的名称即可：
```bash
docker run -it debian
docker run -it alpine
```

### 5. **运行容器时挂载卷（可选）**
如果你想将宿主机的某个目录挂载到容器中以便于数据共享，可以使用 `-v` 参数。例如，将宿主机的 `/host/path` 目录挂载到容器的 `/container/path` 目录：

```bash
docker run -it -v /host/path:/container/path ubuntu
```

### 6. **持久化容器数据**
默认情况下，Docker 容器是无状态的，一旦容器停止或删除，容器内的数据将会丢失。如果你需要持久化数据，可以使用 Docker 卷（volumes）或挂载宿主机目录到容器内。

```bash
docker run -it -v my_volume:/container/data ubuntu
```

这个命令会创建一个名为 `my_volume` 的 Docker 卷，并将其挂载到容器的 `/container/data` 目录下。

### 7. **退出容器**
当你完成对容器的操作后，可以使用以下命令退出容器：

```bash
exit
```

如果你只是想停止容器，但不退出容器，可以使用以下命令：
```bash
docker stop <container_id>
```

你可以通过 `docker ps -a` 查看所有容器的状态，包括运行中的和停止的容器。

### 8. **查看容器日志**
如果你需要查看容器的日志，可以使用以下命令：
```bash
docker logs <container_id>
```

### 9. **删除容器**
如果你不再需要某个容器，可以将其删除：
```bash
docker rm <container_id>
```

如果你想删除对应的镜像，可以使用：
```bash
docker rmi <image_name>
```
### 2. 配置国内镜像

由于 Docker Hub 在中国的访问速度较慢，可以配置使用国内的镜像源。

#### 2.1 使用 Docker Desktop GUI 配置镜像

1. **打开 Docker Desktop**。
2. **点击设置（Settings）**：
   - 在 Docker Desktop 的右上角，点击齿轮图标进入设置页面。
3. **选择 "Docker Engine"**：
   - 在左侧菜单中选择 "Docker Engine"。
4. **修改配置**：
   - 在 JSON 配置中，将 `registry-mirrors` 添加国内镜像地址。以下是一些常用的国内 Docker 镜像源：
     - **阿里云**：`https://<你的阿里云账号>.mirror.aliyuncs.com`
     - **网易**：`https://hub-mirror.c.163.com`
     - **腾讯云**：`https://mirror.ccs.tencentyun.com`
   - 修改后的配置示例：
     ```json
     {
       "registry-mirrors": [
         "https://hub-mirror.c.163.com"
       ]
     }
     ```
5. **点击 "Apply & Restart"** 以应用更改并重启 Docker。