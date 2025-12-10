## GUIA RÁPIDO DOCKER CLI

## GUIA RÁPIDO: Docker CLI

Este guia reúne comandos Docker CLI mais usados. Substitua `IMAGE`, `CONTAINER`, `HOSTPORT`, `CONTAINERPORT`, `HOSTDIR`, `TARGETDIR` e outros placeholders pelos valores reais.

**Sumário**
- [Executar um novo container](#executar-um-novo-container)
- [Gerenciar containers](#gerenciar-containers)
- [Gerenciar imagens](#gerenciar-imagens)
- [Informações e estatísticas](#informacoes-e-estatisticas)

---

### Executar um novo container

Iniciar um novo container (interativo ou padrão):
```bash
docker run IMAGE
docker run nginx
```

Atribuir um nome ao container:
```bash
docker run --name CONTAINER IMAGE
docker run --name web nginx
```

Mapear portas (host -> container):
```bash
docker run -p HOSTPORT:CONTAINERPORT IMAGE
docker run -p 8080:80 nginx
```

Mapear todas as portas expostas pela imagem (porta aleatória no host):
```bash
docker run -P IMAGE
```

Executar em segundo plano (daemon):
```bash
docker run -d IMAGE
docker run -d --name web nginx
```

Definir hostname do container:
```bash
docker run --hostname HOSTNAME IMAGE
```

Adicionar entrada ao /etc/hosts do container:
```bash
docker run --add-host HOSTNAME:IP IMAGE
```

Mapear diretório do host para o container (volume):
```bash
docker run -v /host/dir:/container/dir IMAGE
docker run -v /usr/share/nginx/html:/usr/share/nginx/html:ro -d nginx
```

Alterar ponto de entrada e abrir shell interativo:
```bash
docker run --entrypoint /bin/bash -it IMAGE
docker run -it --entrypoint /bin/bash nginx
```

---

### Gerenciar containers

Listar containers em execução:
```bash
docker ps
```

Listar todos os containers (incluindo parados):
```bash
docker ps -a
```

Parar e iniciar containers:
```bash
docker stop CONTAINER
docker start CONTAINER
```

Remover containers:
```bash
docker rm CONTAINER
docker rm -f CONTAINER   # força remoção
```

Remover todos os containers parados (prompt de confirmação):
```bash
docker container prune
```

Copiar arquivos entre host e container:
```bash
docker cp CONTAINER:SOURCE TARGET   # container -> host
docker cp SOURCE CONTAINER:TARGET   # host -> container
docker cp web:/usr/share/nginx/html/index.html ./index.html
```

Renomear um container:
```bash
docker rename OLD_NAME NEW_NAME
```

Criar uma imagem a partir de um container (commit):
```bash
docker commit CONTAINER IMAGE[:TAG]
docker commit web myimage:latest
```

---

### Gerenciar imagens

Baixar (pull) uma imagem do registry:
```bash
docker pull IMAGE[:TAG]
docker pull nginx:latest
```

Enviar (push) uma imagem para um repositório (autenticado):
```bash
docker push IMAGE[:TAG]
docker push myrepo/myimage:1.0
```

Remover imagens:
```bash
docker rmi IMAGE
```

Listar imagens locais:
```bash
docker images
```

Remover imagens não utilizadas (limpeza):
```bash
docker image prune        # remove imagens dangling
docker image prune -a     # remove todas as imagens não utilizadas
```

Construir uma imagem a partir de um `Dockerfile`:
```bash
docker build -t myimage:latest .
```

Marcar (tag) uma imagem:
```bash
docker tag SOURCE_IMAGE TARGET_IMAGE
docker tag ubuntu ubuntu:18.04
```

Salvar e carregar imagens em arquivo tar:
```bash
docker save -o nginx.tar nginx
docker load -i nginx.tar
```

---

### Informações e estatísticas

Exibir logs de um container:
```bash
docker logs CONTAINER
docker logs -f CONTAINER   # seguir (tail -f)
```

Mostrar estatísticas em tempo real (CPU, memória, I/O):
```bash
docker stats
```

Ver processos em execução dentro de um container:
```bash
docker top CONTAINER
```

Versão do Docker:
```bash
docker version
```

Inspecionar detalhes (config, redes, volumes) de um container ou imagem:
```bash
docker inspect NAME_OR_ID
```

Ver diferenças no sistema de arquivos de um container:
```bash
docker diff CONTAINER
```

Mostrar portas mapeadas de um container:
```bash
docker port CONTAINER
```

---

Se quiser, eu posso:
- adicionar exemplos do `docker-compose`;
- gerar uma versão em PDF/HTML do guia; ou
- incluir atalhos e dicas rápidas no topo.

Fim do guia rápido.
