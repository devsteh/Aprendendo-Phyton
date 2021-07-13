from datetime import date, time, datetime, timedelta

#Data e hora atual
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%w/%Y --- %H:%M:%S'))
    print(data_atual.weekday())#dia da semana, retorna como número
    #pode se atribuir os dias da semana para retorno através de tupla
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2020, 5, 18)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020'
    data_convert = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convert)
    #subtração ou soma de data e hora
    nova_data = data_convert - timedelta(days=365, hours=2, minutes=20)
    print(nova_data)

#Data Manual
def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = (data_atual.strftime('%A/%B/%Y'))
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

#Hora Manual
def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(horario_str)

if __name__ == '__main__':
    #trabalhando_com_time()
    trabalhando_com_datetime()