# 🚀 Blockchain Query Optimization - MVP Simplificado

> Sistema mínimo para demonstração de otimização de consultas em blockchain

---

## 📦 O que é este projeto?

Um **MVP (Produto Mínimo Viável)** que demonstra a diferença de performance entre três métodos de consulta em blockchain:

- **Web3.js**: Consultas diretas à blockchain (lento, mas descentralizado)
- **The Graph**: Indexador descentralizado (equilíbrio)
- **MongoDB**: Banco NoSQL sincronizado (rápido, mas centralizado)

---

## 📁 Estrutura do Projeto

```
blockchain-benchmark-mvp/
├── index.html           # Interface visual (abrir no navegador)
├── app.py              # Backend API (Flask)
├── analyze.py          # Script de análise
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

---

## ⚡ Instalação Rápida (3 minutos)

### Pré-requisitos

- Python 3.8+ instalado
- Navegador web moderno

### Passo 1: Instalar Dependências

```bash
# Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar bibliotecas necessárias
pip install flask flask-cors
```

### Passo 2: Iniciar o Backend

```bash
python app.py
```

Você verá:

```
🚀 Blockchain Query Benchmark - MVP
📡 API rodando em: http://localhost:5000
```

### Passo 3: Abrir Interface

Abra `index.html` no navegador (duplo-clique no arquivo)

---

## 🎯 Como Usar

### 1. Interface Web

1. Abra `index.html` no navegador
2. Clique em **"▶️ Executar Benchmark"**
3. Aguarde alguns segundos
4. Veja os resultados comparativos

### 2. Via API (cURL)

```bash
# Executar benchmark
curl -X POST http://localhost:5000/api/benchmark

# Resposta:
{
  "web3js": 2458,
  "thegraph": 320,
  "mongodb": 67
}
```

### 3. Script de Análise

```bash
python analyze.py
```

Gera:

- Relatório no terminal
- `report.json` com dados estruturados
- `RESULTS.md` com relatório em Markdown

---

## 📊 Resultados Esperados

| Método    | Latência | Speedup vs Web3.js |
| --------- | -------- | ------------------ |
| Web3.js   | ~2.500ms | 1x (baseline)      |
| The Graph | ~320ms   | ~8x mais rápido    |
| MongoDB   | ~67ms    | ~37x mais rápido   |

---

## 💡 Interpretação dos Resultados

### 🔵 Web3.js (Azul)

- **Latência:** Alta (2-3 segundos)
- **Melhor para:** Consultas esporádicas, verificações pontuais
- **Vantagem:** Totalmente descentralizado
- **Desvantagem:** Muito lento para aplicações interativas

### 🟣 The Graph (Roxo)

- **Latência:** Média (250-400ms)
- **Melhor para:** dApps que precisam de descentralização
- **Vantagem:** Bom equilíbrio performance/descentralização
- **Desvantagem:** Custo de queries (GRT tokens)

### 🟢 MongoDB (Verde)

- **Latência:** Baixa (40-80ms)
- **Melhor para:** DeFi, trading, aplicações de alta frequência
- **Vantagem:** Performance máxima
- **Desvantagem:** Requer sincronização e infraestrutura

---

## 🎓 Explicação do Conceito

### Por que as diferenças de performance?

```
┌─────────────────────────────────────────────────────────┐
│  WEB3.JS                                                │
│  ┌────────┐  →  ┌──────────┐  →  ┌─────────┐          │
│  │ dApp   │     │ RPC Node │     │ Ethereum│          │
│  └────────┘     └──────────┘     └─────────┘          │
│  Consulta direta à blockchain (lento)                  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  THE GRAPH                                              │
│  ┌────────┐  →  ┌──────────┐  →  ┌─────────┐          │
│  │ dApp   │     │ Subgraph │     │ Indexer │          │
│  └────────┘     └──────────┘     └─────────┘          │
│  Dados pré-indexados (médio)                           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  MONGODB                                                │
│  ┌────────┐  →  ┌──────────┐                           │
│  │ dApp   │     │ MongoDB  │                           │
│  └────────┘     └──────────┘                           │
│  Consulta em banco otimizado (rápido)                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 Personalização

### Ajustar Simulação de Latência

Edite `app.py`:

```python
def simulate_web3js_query():
    latency = random.randint(2000, 3000)  # Altere estes valores
    return latency
```

### Adicionar Mais Métricas

Edite `analyze.py` para calcular:

- Desvio padrão
- Percentis (p95, p99)
- Custo estimado

---

## 📝 Arquivos Gerados

Após executar `analyze.py`:

- **`report.json`**: Dados estruturados para processamento
- **`RESULTS.md`**: Relatório legível em Markdown

---

## 🐛 Troubleshooting

### Erro: "Port 5000 already in use"

```bash
# Mudar porta em app.py
app.run(port=5001)  # Use 5001 em vez de 5000
```

### Erro: "CORS blocked"

Certifique-se de que:

1. `flask-cors` está instalado
2. O backend está rodando
3. Você está acessando `index.html` localmente

### Interface não conecta com API

Verifique no `index.html`:

```javascript
fetch("http://localhost:5000/api/benchmark");
// Trocar 5000 pela porta correta se necessário
```

---

## 📚 Para Apresentação

### Roteiro de Demonstração (5 minutos)

1. **Contexto** (1 min)

   - Problema: Consultas em blockchain são lentas
   - Objetivo: Comparar soluções

2. **Demo** (2 min)

   - Mostrar interface
   - Executar benchmark
   - Explicar resultados visuais

3. **Análise** (1 min)

   - Mostrar relatório gerado
   - Destacar diferenças de performance

4. **Conclusão** (1 min)
   - MongoDB: 37x mais rápido
   - Trade-off: performance vs descentralização
   - Cada método tem seu uso ideal

---

## 🚀 Próximos Passos (Fora do MVP)

Para expandir este MVP:

- [ ] Conectar com blockchain real (via Infura)
- [ ] Adicionar mais tipos de consulta
- [ ] Implementar cache inteligente
- [ ] Testes com contratos reais (USDT, USDC)
- [ ] Métricas de custo (gas fees)

---

## 📄 Licença

MIT License - Livre para uso acadêmico e comercial

---

## 📧 Suporte

Problemas ou dúvidas?

- Abra uma issue no GitHub
- Consulte a documentação do Flask: https://flask.palletsprojects.com/

---

**⭐ Dica:** Para apresentações, mantenha o foco nos resultados visuais do gráfico de barras - a diferença é clara e impactante!
