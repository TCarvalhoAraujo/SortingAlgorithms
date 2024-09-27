
# Relatório de Análise de Algoritmos de Ordenação

## Metodologia Utilizada
Este experimento foi conduzido para comparar os tempos de execução de três algoritmos de ordenação: **Heap Sort**, **Insertion Sort**, e **Merge Sort**. Para cada algoritmo, foi utilizado um conjunto de arrays de tamanhos variáveis para medir o desempenho. Os tamanhos dos arrays foram selecionados como potências de 3 para Heap Sort e Insertion Sort, e potências de 5 para Merge Sort.

Os passos principais da metodologia foram:
- Para cada algoritmo, foram gerados arrays de números aleatórios dentro de um intervalo pré-definido.
- O tempo de execução para ordenar cada array foi registrado utilizando a função `time.time()`.
- Os resultados foram coletados e analisados para identificar o comportamento de cada algoritmo com diferentes tamanhos de entrada.

## Análise dos Resultados
- **Insertion Sort**: Como esperado, o Insertion Sort apresentou tempos de execução crescentes à medida que o tamanho do array aumentava. Este algoritmo, com complexidade \(O(n^2)\), mostrou-se adequado apenas para pequenos conjuntos de dados. Para entradas maiores, como \(3^{10}\), o tempo de execução foi substancialmente elevado.
  
- **Heap Sort**: O Heap Sort manteve uma eficiência estável, mas à medida que os arrays cresceram em tamanho, ele começou a demonstrar sinais de aumento no tempo de execução. Mesmo sendo \(O(n \log n)\), ele não foi tão rápido quanto o Merge Sort para grandes entradas.

- **Merge Sort**: O Merge Sort apresentou o melhor desempenho nos testes realizados, mantendo tempos de execução baixos, especialmente para grandes tamanhos de entrada. Sua complexidade \(O(n \log n)\) se mostrou vantajosa para arrays grandes.

### Comparação Gráfica dos Tempos de Execução:
Foi gerado um gráfico para cada algoritmo, comparando seus tempos de execução em diferentes tamanhos de arrays. Isso facilitou a análise visual de como os tempos de execução aumentam com o tamanho da entrada.

## Conclusões
Com base nos resultados obtidos, pode-se concluir que:
- O **Merge Sort** é o algoritmo mais eficiente entre os três para grandes conjuntos de dados, devido à sua capacidade de dividir e conquistar com complexidade \(O(n \log n)\).
- O **Heap Sort** se comportou de maneira eficiente em tamanhos menores, mas apresentou crescimento mais acentuado do tempo de execução para entradas maiores em comparação com o Merge Sort.
- O **Insertion Sort** é adequado apenas para entradas pequenas, uma vez que seu tempo de execução cresce rapidamente com o aumento do tamanho dos arrays.

Esses resultados confirmam o comportamento esperado dos algoritmos, com o Merge Sort sendo o mais eficiente para entradas maiores.
