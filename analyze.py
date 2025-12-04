#!/usr/bin/env python3
"""
Script de Análise Simples
Gera relatório básico com resultados do benchmark
"""

import json
import time
from datetime import datetime

# ============================================================================
# DADOS DE EXEMPLO (em produção, viriam da API)
# ============================================================================

SAMPLE_RESULTS = {
    "executions": [
        {"web3js": 2458, "thegraph": 320, "mongodb": 67},
        {"web3js": 2621, "thegraph": 298, "mongodb": 72},
        {"web3js": 2534, "thegraph": 315, "mongodb": 69},
        {"web3js": 2489, "thegraph": 335, "mongodb": 64},
        {"web3js": 2598, "thegraph": 302, "mongodb": 71}
    ]
}

# ============================================================================
# FUNÇÕES DE ANÁLISE
# ============================================================================

def calculate_average(results, method):
    """Calcula média de latência para um método"""
    values = [r[method] for r in results]
    return sum(values) / len(values)

def calculate_speedup(baseline, compared):
    """Calcula speedup (quantas vezes mais rápido)"""
    return baseline / compared

def generate_report(results):
    """Gera relatório em texto"""
    
    print("=" * 70)
    print("📊 RELATÓRIO DE BENCHMARK - BLOCKCHAIN QUERY OPTIMIZATION")
    print("=" * 70)
    print(f"\n🕐 Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"🔢 Execuções: {len(results)}")
    
    # Calcula médias
    web3js_avg = calculate_average(results, 'web3js')
    thegraph_avg = calculate_average(results, 'thegraph')
    mongodb_avg = calculate_average(results, 'mongodb')
    
    print("\n" + "─" * 70)
    print("📈 LATÊNCIA MÉDIA (ms)")
    print("─" * 70)
    print(f"  Web3.js:    {web3js_avg:.1f}ms  ⭐")
    print(f"  The Graph:  {thegraph_avg:.1f}ms  ⭐⭐⭐")
    print(f"  MongoDB:    {mongodb_avg:.1f}ms  ⭐⭐⭐⭐⭐")
    
    # Calcula speedups
    speedup_graph = calculate_speedup(web3js_avg, thegraph_avg)
    speedup_mongo = calculate_speedup(web3js_avg, mongodb_avg)
    
    print("\n" + "─" * 70)
    print("⚡ SPEEDUP (em relação ao Web3.js)")
    print("─" * 70)
    print(f"  The Graph:  {speedup_graph:.1f}x mais rápido")
    print(f"  MongoDB:    {speedup_mongo:.1f}x mais rápido")
    
    # Recomendações
    print("\n" + "─" * 70)
    print("💡 RECOMENDAÇÕES")
    print("─" * 70)
    print("""
  🎯 DeFi / Trading de Alta Frequência
     → Use MongoDB (latência mínima essencial)
  
  🌐 dApps Descentralizadas
     → Use The Graph (equilíbrio performance/descentralização)
  
  🔍 Consultas Pontuais / Wallets
     → Use Web3.js (simplicidade e descentralização máxima)
    """)
    
    print("=" * 70)
    
    return {
        'web3js_avg': web3js_avg,
        'thegraph_avg': thegraph_avg,
        'mongodb_avg': mongodb_avg,
        'speedup_graph': speedup_graph,
        'speedup_mongo': speedup_mongo
    }

def save_report_json(results, stats, filename='report.json'):
    """Salva relatório em JSON"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'executions': len(results),
        'averages': {
            'web3js': stats['web3js_avg'],
            'thegraph': stats['thegraph_avg'],
            'mongodb': stats['mongodb_avg']
        },
        'speedup': {
            'thegraph_vs_web3js': stats['speedup_graph'],
            'mongodb_vs_web3js': stats['speedup_mongo']
        },
        'raw_results': results
    }
    
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n💾 Relatório salvo em: {filename}")

def generate_markdown(stats, filename='RESULTS.md'):
    """Gera relatório em Markdown"""
    
    markdown = f"""# Relatório de Benchmark

**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## Resultados

### Latência Média

| Método | Latência | Performance |
|--------|----------|-------------|
| Web3.js | {stats['web3js_avg']:.1f}ms | ⭐ |
| The Graph | {stats['thegraph_avg']:.1f}ms | ⭐⭐⭐ |
| MongoDB | {stats['mongodb_avg']:.1f}ms | ⭐⭐⭐⭐⭐ |

### Speedup

- **The Graph**: {stats['speedup_graph']:.1f}x mais rápido que Web3.js
- **MongoDB**: {stats['speedup_mongo']:.1f}x mais rápido que Web3.js

## Conclusões

1. **MongoDB** oferece a melhor performance absoluta
2. **The Graph** mantém bom equilíbrio entre performance e descentralização
3. **Web3.js** adequado apenas para consultas esporádicas

## Recomendações

### DeFi / Trading
→ **MongoDB** - Latência crítica para UX

### dApps
→ **The Graph** - Equilíbrio ideal

### Consultas Pontuais
→ **Web3.js** - Simplicidade e descentralização
"""
    
    with open(filename, 'w') as f:
        f.write(markdown)
    
    print(f"📄 Relatório Markdown salvo em: {filename}")

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

def main():
    """Função principal"""
    
    print("\n🔬 Analisando resultados do benchmark...\n")
    time.sleep(0.5)
    
    # Gera relatório
    stats = generate_report(SAMPLE_RESULTS['executions'])
    
    # Salva em diferentes formatos
    save_report_json(SAMPLE_RESULTS['executions'], stats)
    generate_markdown(stats)
    
    print("\n✅ Análise concluída!\n")

if __name__ == '__main__':
    main()