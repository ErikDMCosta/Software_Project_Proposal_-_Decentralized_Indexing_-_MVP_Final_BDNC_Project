#!/usr/bin/env python3
"""
Blockchain Query Benchmark - MVP Simplificado
Backend mínimo para demonstração do conceito
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import random

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

# ============================================================================
# SIMULAÇÃO SIMPLES DOS TRÊS MÉTODOS
# ============================================================================

def simulate_web3js_query():
    """Simula consulta via Web3.js (lenta)"""
    time.sleep(0.5)  # Simula latência
    latency = random.randint(2000, 3000)  # 2-3 segundos
    return latency

def simulate_thegraph_query():
    """Simula consulta via The Graph (média)"""
    time.sleep(0.1)  # Simula latência
    latency = random.randint(250, 400)  # 250-400ms
    return latency

def simulate_mongodb_query():
    """Simula consulta via MongoDB (rápida)"""
    time.sleep(0.02)  # Simula latência
    latency = random.randint(40, 80)  # 40-80ms
    return latency

# ============================================================================
# ENDPOINTS DA API
# ============================================================================

@app.route('/api/benchmark', methods=['POST'])
def run_benchmark():
    """
    Executa benchmark simplificado
    
    Retorna latência em ms para cada método
    """
    print("🚀 Iniciando benchmark...")
    
    results = {
        'web3js': simulate_web3js_query(),
        'thegraph': simulate_thegraph_query(),
        'mongodb': simulate_mongodb_query()
    }
    
    print(f"✅ Resultados: {results}")
    
    return jsonify(results)

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'ok',
        'message': 'API rodando!'
    })

@app.route('/')
def home():
    """Página inicial com instruções"""
    return """
    <html>
    <head>
        <title>Blockchain Benchmark API</title>
        <style>
            body { 
                font-family: Arial; 
                max-width: 800px; 
                margin: 50px auto; 
                padding: 20px;
                background: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 { color: #667eea; }
            .endpoint {
                background: #f9fafb;
                padding: 15px;
                border-radius: 5px;
                margin: 10px 0;
                border-left: 4px solid #667eea;
            }
            code {
                background: #e5e7eb;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔍 Blockchain Query Benchmark API</h1>
            <p>API mínima para demonstração de benchmarks</p>
            
            <h2>📡 Endpoints Disponíveis</h2>
            
            <div class="endpoint">
                <strong>POST /api/benchmark</strong><br>
                Executa benchmark e retorna latências
            </div>
            
            <div class="endpoint">
                <strong>GET /api/health</strong><br>
                Verifica status da API
            </div>
            
            <h2>💻 Como Usar</h2>
            <p>1. Abra <code>index.html</code> no navegador</p>
            <p>2. Clique em "Executar Benchmark"</p>
            <p>3. Veja os resultados comparativos</p>
            
            <h2>🧪 Teste Manual</h2>
            <p>Execute no terminal:</p>
            <code>curl -X POST http://localhost:5000/api/benchmark</code>
        </div>
    </body>
    </html>
    """

# ============================================================================
# INICIALIZAÇÃO
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Blockchain Query Benchmark - MVP")
    print("=" * 60)
    print("\n📡 API rodando em: http://localhost:5000")
    print("🌐 Abra index.html no navegador para usar o dashboard\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )