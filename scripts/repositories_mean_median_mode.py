import csv

# Definir o caminho para o arquivo CSV
file_path = "repositories_info.csv"

# Inicializar variáveis para armazenar dados
data = []
rq1 = []  # RQ1 - Idade do repositório (dias)
rq2 = []  # RQ2 - Total de pull requests aceitos
rq3 = []  # RQ3 - Total de releases
rq4 = []  # RQ4 - Tempo desde a última atualização (dias)
rq5 = []  # RQ5 - Linguagem principal
rq6 = []  # RQ6 - Porcentagem de issues fechadas

# Ler os dados do CSV
with open(file_path, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)  # Pular a linha do cabeçalho
    for row in reader:
        data.append(row)
        rq1.append(int(row[1]))
        rq2.append(int(row[2]))
        rq3.append(int(row[3]))
        rq4.append(int(row[4]))
        rq5.append(row[5])
        rq6.append(float(row[6]))

# Calcular média, mediana e moda para cada conjunto de dados
import statistics

def calculate_statistics(data_set):
    try:
        mean = statistics.mean(data_set)
        median = statistics.median(data_set)
        mode = statistics.mode(data_set)
        return f"Média: {mean:.2f}, Mediana: {median}, Moda: {mode}"
    except statistics.StatisticsError:
        return "Dados insuficientes para calcular estatísticas."  # Lidar com casos com dados insuficientes

# Imprimir os resultados
print("RQ1 - Idade do Repositório (dias):")
print(calculate_statistics(rq1))
print("RQ2 - Total de Pull Requests Aceitos:")
print(calculate_statistics(rq2))
print("RQ3 - Total de Releases:")
print(calculate_statistics(rq3))
print("RQ4 - Tempo Desde a Última Atualização (dias):")
print(calculate_statistics(rq4))
print("RQ5 - Linguagem Principal:")
# Moda não aplicável para dados categóricos como linguagem principal
print(f"Linguagem mais frequente: {statistics.mode(rq5)}")
print("RQ6 - Porcentagem de Issues Fechadas:")
print(calculate_statistics(rq6))

