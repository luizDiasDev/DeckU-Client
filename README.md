<img width="1640" height="856" alt="deckullt" src="https://github.com/user-attachments/assets/a29deb14-6a4d-4f89-8b7d-0018f05ef310" />


https://github.com/user-attachments/assets/544cfba0-743e-483d-837c-1a5357ea8593


# DeckU - Client

Parte do projeto **DeckU**: transformar um Steam Deck em um controle e uma segunda tela estilo WiiU GamePad para o PC.

Este repositório contém o **cliente**, que roda no Steam Deck. Ele é responsável por ler os inputs físicos do controle e enviá-los pela rede para o [DeckU-Server](https://github.com/luizDiasDev/DeckU-Server), que roda no PC.

> O repositório do servidor (parte que roda no PC) está aqui: **[DeckU-Server](https://github.com/luizDiasDev/DeckU-Server)**

---

## 💡 Sobre o projeto

A ideia surgiu como um desafio pessoal de aprendizado para sair da zona de conforto e aprender programação na prática — sockets, leitura de hardware, POO, boas práticas, tudo isso construído do zero, sem tutorial pronto pra seguir.

---

## ⚙️ O que esse cliente faz hoje

- Lê os eventos de input do controle físico do Steam Deck via **evdev** (Linux), direto do `/dev/input/eventX`.
- Mapeia os códigos de evento para os botões e analógicos correspondentes (todos os botões básicos de um controle convencional: A, B, X, Y, L1, R1, L2, R2, Start, Select, D-pad e analógicos).
- Aplica uma **deadzone** nos analógicos para filtrar o drift natural do hardware.
- Envia o estado atual do controle via **socket UDP**, serializado em **JSON**, para o servidor rodando no PC.

## 🚧 O que ainda falta / limitações conhecidas

- **Perda ocasional de pacotes**: por usar UDP (escolha intencional, priorizando baixa latência sobre garantia de entrega), às vezes um pacote se perde e o controle demora um instante para "voltar ao normal". É um ponto que pretendo melhorar.
- **Trackpads e giroscópio** do Deck ainda não estão mapeados — só os inputs "convencionais" de controle por enquanto.
- A parte de **transmissão de tela** (o Deck funcionando como uma segunda tela, ao estilo WiiU) ainda **não está integrada no código** — hoje isso é validado com ferramentas externas (Virtual Display Driver + ffmpeg rodando manualmente), sem nenhuma automação em Python ainda. Essa é a próxima grande etapa do projeto.
- Ainda não há tratamento robusto de reconexão caso a rede caia.

---

## 🏗️ Arquitetura

O projeto é organizado em classes com responsabilidades separadas:

- **`Gamepad`**: lê e interpreta os eventos do controle físico, mantendo o estado atual (`gamepad_output`). Não sabe nada sobre rede.
- **`Sender`**: responsável por serializar e enviar dados via UDP. Não sabe nada sobre controle.
- **`main.py`**: orquestra as duas classes através de um **callback** — o `Gamepad` avisa quando o estado muda, e o `main.py` decide o que fazer com essa informação (nesse caso, repassar pro `Sender`).

Essa separação segue o princípio de responsabilidade única: cada classe faz uma coisa só, e pode evoluir/ser substituída sem afetar as outras.

---

## 🔧 Tecnologias

- **Python 3.13**
- [`evdev`](https://python-evdev.readthedocs.io/) — leitura de eventos de input no Linux
- `socket` (biblioteca padrão) — comunicação via UDP
- `json` (biblioteca padrão) — serialização dos dados
- `python-dotenv` — gerenciamento de configuração via variáveis de ambiente

---

## ▶️ Como rodar

1. Clone o repositório no seu Steam Deck (modo Desktop):
   ```bash
   git clone https://github.com/luizDiasDev/DeckU-Client.git
   cd DeckU-Client
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto com as configurações (veja `.env.example`):
   ```
   PC_IP=192.168.x.x
   PORT=5005
   DEVICE_PATH=/dev/input/eventX
   ```
   > Use `evtest` para descobrir qual `/dev/input/eventX` corresponde ao controle do Deck.

4. Rode:
   ```bash
   python main.py
   ```

---

## 📌 Status

🟡 **MVP funcional** — controle já é reconhecido e utilizável no PC via servidor virtual (vgamepad), com espaço para otimização de estabilidade e expansão de inputs.

---

## 🗺️ Próximos passos

- [ ] Mapear trackpads e giroscópio
- [ ] Melhorar estabilidade da conexão (lidar com perda de pacotes)
- [ ] Integrar captura e streaming de tela no próprio código Python (hoje depende de ferramentas externas)
- [ ] Reduzir latência geral do input

---

## 👤 Autor

**Luiz Dias**
Projeto pessoal de aprendizado em Python, redes e programação orientada a objetos.
