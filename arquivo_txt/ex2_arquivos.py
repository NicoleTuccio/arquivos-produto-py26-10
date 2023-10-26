import oracledb as db

user="rm99711"
pwd="290204"
dsn = "oracle.fiap.com.br/orcl"

try:
    lista = []
    with open('faturamento.txt', 'r') as arq:
        for linha in arq:
            dado = linha.replace("\n", '').split(";") #para separar
            dicionario = {
                "prod": dado[0],
                "marca": dado[1],
                "loja": dado[2],
                "data": dado[3], 
                "quantidade":int(dado[4]),
                "valor": float(dado[5])
            }
            
            lista.append(dicionario)#adicionar o dicionario recém criado na lista
        
    #print(lista)
    with db.connect(user=user, password = pwd, dsn=dsn) as con:
        sql = '''INSERT INTO faturamento(id, produto, marca, loja, 
        data, quantidade, valor) VALUES (gerador_id.NEXTVAL,
        :prod, :marca, :loja, to_date(:data, 'YYYY-MM-DD'),  
        :quantidade, :valor)''' #to_date-> formato, :data-> o que vai ser motificado, o formato q esta a data
        with con.cursor() as cur:
            for registro in lista:
                cur.execute(sql, registro)
            con.commit()#precisa dar comit se não nenum dado vai ser registrado

    print("Registros Inseridos")

except Exception as erro:
    print(erro)