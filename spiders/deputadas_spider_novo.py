from wsgiref import headers
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "meu_raspador_deputadas"

    def start_requests(self):
        urls = [
                'https://www.camara.leg.br/deputados/178989',
                'https://www.camara.leg.br/deputados/204525',
                'https://www.camara.leg.br/deputados/178945',
                'https://www.camara.leg.br/deputados/204535',
                'https://www.camara.leg.br/deputados/178961',
                'https://www.camara.leg.br/deputados/204360',
                'https://www.camara.leg.br/deputados/178946',
                'https://www.camara.leg.br/deputados/204534',
                'https://www.camara.leg.br/deputados/204464',
                'https://www.camara.leg.br/deputados/178901',
                'https://www.camara.leg.br/deputados/204466',
                'https://www.camara.leg.br/deputados/178862',
                'https://www.camara.leg.br/deputados/215044',
                'https://www.camara.leg.br/deputados/74075',
                'https://www.camara.leg.br/deputados/220008',
                'https://www.camara.leg.br/deputados/218086',
                'https://www.camara.leg.br/deputados/160575',
                'https://www.camara.leg.br/deputados/204407',
                'https://www.camara.leg.br/deputados/204354',
                'https://www.camara.leg.br/deputados/160598',
                'https://www.camara.leg.br/deputados/204447',
                'https://www.camara.leg.br/deputados/178966',
                'https://www.camara.leg.br/deputados/107283',
                'https://www.camara.leg.br/deputados/129618',
                'https://www.camara.leg.br/deputados/198197',
                'https://www.camara.leg.br/deputados/67138',
                'https://www.camara.leg.br/deputados/74848',
                'https://www.camara.leg.br/deputados/108338',
                'https://www.camara.leg.br/deputados/178839',
                'https://www.camara.leg.br/deputados/204468',
                'https://www.camara.leg.br/deputados/204546',
                'https://www.camara.leg.br/deputados/74856',
                'https://www.camara.leg.br/deputados/160534',
                'https://www.camara.leg.br/deputados/178832',
                'https://www.camara.leg.br/deputados/204375',
                'https://www.camara.leg.br/deputados/139285',
                'https://www.camara.leg.br/deputados/204405',
                'https://www.camara.leg.br/deputados/204410',
                'https://www.camara.leg.br/deputados/74784',
                'https://www.camara.leg.br/deputados/178866',
                'https://www.camara.leg.br/deputados/166402',
                'https://www.camara.leg.br/deputados/204458',
                'https://www.camara.leg.br/deputados/204471',
                'https://www.camara.leg.br/deputados/204430',
                'https://www.camara.leg.br/deputados/171619',
                'https://www.camara.leg.br/deputados/74398',
                'https://www.camara.leg.br/deputados/204540',
                'https://www.camara.leg.br/deputados/178956',
                'https://www.camara.leg.br/deputados/204428',
                'https://www.camara.leg.br/deputados/204432',
                'https://www.camara.leg.br/deputados/204453',
                'https://www.camara.leg.br/deputados/66179',
                'https://www.camara.leg.br/deputados/216198',
                'https://www.camara.leg.br/deputados/205535',
                'https://www.camara.leg.br/deputados/204377',
                'https://www.camara.leg.br/deputados/73943',
                'https://www.camara.leg.br/deputados/204529',
                'https://www.camara.leg.br/deputados/204565',
                'https://www.camara.leg.br/deputados/160639',
                'https://www.camara.leg.br/deputados/160641',
                'https://www.camara.leg.br/deputados/204467',
                'https://www.camara.leg.br/deputados/215361',
                'https://www.camara.leg.br/deputados/178925',
                'https://www.camara.leg.br/deputados/204528',
                'https://www.camara.leg.br/deputados/204545',
                'https://www.camara.leg.br/deputados/74057',
                'https://www.camara.leg.br/deputados/204353',
                'https://www.camara.leg.br/deputados/204400',
                'https://www.camara.leg.br/deputados/73696',
                'https://www.camara.leg.br/deputados/123756',
                'https://www.camara.leg.br/deputados/204509',
                'https://www.camara.leg.br/deputados/73701',
                'https://www.camara.leg.br/deputados/207176',
                'https://www.camara.leg.br/deputados/204374',
                'https://www.camara.leg.br/deputados/160589',
                'https://www.camara.leg.br/deputados/213762',
                'https://www.camara.leg.br/deputados/204507',
                'https://www.camara.leg.br/deputados/164360',
                'https://www.camara.leg.br/deputados/204369',
                'https://www.camara.leg.br/deputados/204380',
                'https://www.camara.leg.br/deputados/204462',
                'https://www.camara.leg.br/deputados/178928',
                'https://www.camara.leg.br/deputados/178939',
                'https://www.camara.leg.br/deputados/204459',
                'https://www.camara.leg.br/deputados/81297',
                'https://www.camara.leg.br/deputados/204434',
                'https://www.camara.leg.br/deputados/178994',
                'https://www.camara.leg.br/deputados/204421',
                'https://www.camara.leg.br/deputados/204357',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       
        filename = f'test_deputadas.html'
        # dep =  response.css('body').getall()
        #dep_nome = response.xpath('//h2[@id="nomedeputado"]/text()').extract()
        #print(str(dep_nome))
        
        nome = response.css("ul.informacoes-deputado").getall()
        print("------------------------")
        nome = Selector(text=nome[0]).xpath('//li/text()').get()
        nome = nome.strip()
        print(nome)
        
        presenca_plenario = response.xpath('//*[@id="atuacao-section"]/div[2]/ul[2]/li[1]/dl/dd[1]/text()').get()
        presenca_plenario = str(presenca_plenario).strip().split()[0]
        print("presença plenário: "+presenca_plenario)
        
        print("------------------------")
        
        #ausencia_plenario
            #ausencia_nao_justificada
        ausencia_plenario_nj = response.xpath('//*[@id="atuacao-section"]/div[2]/ul[2]/li[1]/dl/dd[3]/text()').get()
        ausencia_plenario_nj = str(ausencia_plenario_nj).strip().split()[0]
        
            #ausencia_justificada
        ausencia_plenario_j = response.xpath('//*[@id="atuacao-section"]/div[2]/ul[2]/li[1]/dl/dd[2]/text()').get()
        ausencia_plenario_j = str(ausencia_plenario_j).strip().split()[0]
        
        ausencia_plenario = 0
        
        if (ausencia_plenario_nj != 'None' and ausencia_plenario_j != 'None'):
            ausencia_plenario = int(ausencia_plenario_nj)+int(ausencia_plenario_j)
        
        if (ausencia_plenario_nj == 'None' and ausencia_plenario_j != 'None'):
            ausencia_plenario = int(ausencia_plenario_j)
            
        if (ausencia_plenario_nj != 'None' and ausencia_plenario_j == 'None'):
            ausencia_plenario = int(ausencia_plenario_nj)
        
        print("ausencia plenário: ",ausencia_plenario)
        
        print("------------------------")
        
        #ausencia_justificada_plenario
        
        print("ausencia plenário: "+str(ausencia_plenario_j))
        
        print("------------------------")
        #presenca_comissao
        
        presenca_comissao = response.xpath('//*[@id="atuacao-section"]/div[2]/ul[2]/li[2]/dl/dd[1]/text()').get()
        presenca_comissao = str(presenca_plenario).strip().split()[0]
        print("presença comissao: "+presenca_comissao)
        
        print("------------------------")
        #ausencia_comissao
        
        #ausencia_comissao
            #ausencia_nao_justificada
        ausencia_comissao_nj = response.xpath('//*[@id="atuacao-section"]/div[2]/ul[2]/li[2]/dl/dd[3]/text()').get()
        ausencia_comissao_nj = str(ausencia_comissao_nj).strip().split()[0]
        
            #ausencia_justificada
        ausencia_comissao_j = response.xpath('//*[@id="atuacao-section"]/div[2]/ul[2]/li[2]/dl/dd[2]/text()').get()
        ausencia_comissao_j = str(ausencia_comissao_j).strip().split()[0]
        
       
        
        ausencia_comissao = int(ausencia_comissao_nj) + int(ausencia_comissao_j)
            
        print("ausencia_comissao: ",ausencia_comissao)
        
        print("------------------------")
        #ausencia_justificada_comissao
        
        print("ausencia justificaa comissao: "+str(ausencia_comissao_j))
        
        print("------------------------")
        #data_nascimento
        
        data_nascimento = response.css("ul.informacoes-deputado").getall()
        print("------------------------")
        data_nascimento = Selector(text=data_nascimento[0]).xpath('//li/text()').getall()[4]
        data_nascimento = data_nascimento.strip()
        
        print("data_nascimento: "+data_nascimento)
        
        print("------------------------")
        #gasto_total_par
        
        
        gasto_total_par = response.xpath('//*[@id="percentualgastocotaparlamentar"]/tbody/tr[1]/td[2]/text()').get()
        gasto_total_par = str(gasto_total_par).strip()
        print("gasto total par: "+gasto_total_par)
        
        print("------------------------")
        
        #Criando um dicionário para obter os valores dos meses
        #Cada par vai ter o nome do mês e o valor vai ser o gasto no mês
        #Feito com dicionário para garantir a preservação da ordem dos meses
        dicionario_par = {}
        
        #gasto_jan_par
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[1]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[1]/td[2]/text()').get()
        
        #gasto_fev_par
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[2]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[2]/td[2]/text()').get()
        
        #gasto_mar_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[3]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[3]/td[2]/text()').get()
        
        #gasto_abr_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[4]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[4]/td[2]/text()').get()
        
        #gasto_maio_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[5]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[5]/td[2]/text()').get()
        
        #gasto_junho_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[6]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[6]/td[2]/text()').get()
        
        #gasto_jul_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[7]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[7]/td[2]/text()').get()
        
        #gasto_agosto_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[8]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[8]/td[2]/text()').get()
        
        #gasto_set_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[9]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[9]/td[2]/text()').get()
        
        #gasto_out_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[10]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[10]/td[2]/text()').get()
        
        #gasto_nov_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[11]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[11]/td[2]/text()').get()
        
        #gasto_dez_par
        
        dicionario_par[response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[12]/td[1]/text()').get()] = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[12]/td[2]/text()').get()
        
        #setando as variaveis de acordo com o dicionário
        
        
        if 'JAN' in dicionario_par:
            gasto_jan_par = str(dicionario_par['JAN']).strip()
        else:
            gasto_jan_par = '0'
            
        if 'FEV' in dicionario_par:
            gasto_fev_par = str(dicionario_par['FEV']).strip()
        else:
            gasto_fev_par = '0'
            
        if 'MAR' in dicionario_par:
            gasto_mar_par = str(dicionario_par['MAR']).strip()
        else:
            gasto_mar_par = '0'
        
        if 'ABR' in dicionario_par:
            gasto_abr_par = str(dicionario_par['ABR']).strip()
        else:
            gasto_abr_par = '0'
            
        if 'MAI' in dicionario_par:
            gasto_maio_par = str(dicionario_par['MAI']).strip()
        else:
            gasto_maio_par = '0'
            
        if 'JUN' in dicionario_par:
            gasto_junho_par = str(dicionario_par['JUN']).strip()
        else:
            gasto_junho_par = '0'
            
        if 'JUL' in dicionario_par:
            gasto_jul_par = str(dicionario_par['JUL']).strip()
        else:
            gasto_jul_par = '0'
            
        if 'AGO' in dicionario_par:
            gasto_agosto_par = str(dicionario_par['AGO']).strip()
        else:
            gasto_agosto_par = '0'

        if 'SET' in dicionario_par:
            gasto_set_par = str(dicionario_par['SET']).strip()
        else:
            gasto_set_par = '0'

        if 'OUT' in dicionario_par:
            gasto_out_par = str(dicionario_par['OUT']).strip()
        else:
            gasto_out_par = '0'
            
        if 'NOV' in dicionario_par:
            gasto_nov_par = str(dicionario_par['NOV']).strip()
        else:
            gasto_nov_par = '0'
        
        if 'DEZ' in dicionario_par:
            gasto_dez_par = str(dicionario_par['DEZ']).strip()
        else:
            gasto_dez_par = '0'
  
        #gasto_total_gab
        
        gasto_total_gab = response.xpath('//*[@id="percentualgastoverbagabinete"]/tbody/tr[1]/td[2]/text()').get()
        gasto_total_gab = str(gasto_total_gab).strip()
        print("gasto total gab: "+gasto_total_gab)
        
        
        print("------------------------")
        #gasto_jan_gab
        
        
        gasto_jan_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[1]/td[2]/text()').get()
        gasto_jan_gab = str(gasto_jan_gab).strip()
        print("gasto jan gab: "+gasto_jan_gab)
        
        print("------------------------")
        #gasto_fev_gab
        
        gasto_fev_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[2]/td[2]/text()').get()
        gasto_fev_gab = str(gasto_fev_gab).strip()
        print("gasto fev gab: "+gasto_fev_gab)
        
        #gasto_mar_gab
        
        gasto_mar_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[3]/td[2]/text()').get()
        gasto_mar_gab = str(gasto_mar_gab).strip()
        print("gasto mar gab: "+gasto_mar_gab)
        
        print("------------------------")
        #gasto_abr_gab
        
        gasto_abr_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[4]/td[2]/text()').get()
        gasto_abr_gab = str(gasto_abr_gab).strip()
        print("gasto abr gab: "+gasto_abr_gab)
        
        
        #gasto_maio_gab
        
        gasto_maio_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[5]/td[2]/text()').get()
        gasto_maio_gab = str(gasto_maio_gab).strip()
        print("gasto maio gab: "+gasto_maio_gab)
        
        print("------------------------")
        #gasto_junho_gab
        
        gasto_junho_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[6]/td[2]/text()').get()
        gasto_junho_gab = str(gasto_junho_gab).strip()
        print("gasto junho gab: "+gasto_junho_gab)
        
        print("------------------------")
        #gasto_julho_gab
        
        gasto_julho_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[7]/td[2]/text()').get()
        gasto_julho_gab = str(gasto_julho_gab).strip()
        print("gasto julho gab: "+gasto_julho_gab)
        
        print("------------------------")
        #gasto_agosto_gab
        
        gasto_agosto_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[8]/td[2]/text()').get()
        gasto_agosto_gab = str(gasto_agosto_gab).strip()
        print("gasto agosto gab: "+gasto_agosto_gab)
        
        print("------------------------")
        #gasto_set_gab
        
        gasto_set_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[9]/td[2]/text()').get()
        gasto_set_gab = str(gasto_set_gab).strip()
        print("gasto set gab: "+gasto_set_gab)
        
        print("------------------------")
        #gasto_out_gab
        
        gasto_out_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[10]/td[2]/text()').get()
        gasto_out_gab = str(gasto_out_gab).strip()
        print("gasto out gab: "+gasto_out_gab)
        
        print("------------------------")
        #gasto_nov_gab
        
        gasto_nov_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[11]/td[2]/text()').get()
        gasto_nov_gab = str(gasto_nov_gab).strip()
        print("gasto nov gab: "+gasto_nov_gab)
        
        print("------------------------")
        #gasto_dez_gab
        
        gasto_dez_gab = response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr[12]/td[2]/text()').get()
        gasto_dez_gab = str(gasto_dez_gab).strip()
        print("gasto dez gab: "+gasto_dez_gab)
        
        print("------------------------")
        #salario_bruto
        salario_bruto_par = response.xpath('//*[@id="recursos-section"]/ul/li[2]/div/a/text()').get()
        salario_bruto_par_result = salario_bruto_par.split()[1]
        print("salario bruto par: "+salario_bruto_par_result)
        
        print("------------------------")
        #quant_viagem
        
        quant_viagem = response.xpath('//*[@id="recursos-section"]/ul/li[5]/div/span/text()').get()
        
        print("qtd viagem: ",quant_viagem)
        
        print("------------------------")
        
        yield {
                'nome': nome ,
                'sexo': "F",
                'presenca_plenario': presenca_plenario,
                'ausencia_plenario': ausencia_plenario,
                'ausencia_justificada_plenario': ausencia_plenario_j,
                'presenca_comissao':presenca_comissao,
                'ausencia_comissao':ausencia_comissao,
                'ausencia_justificada_comissao':ausencia_comissao_j,
                'data_nascimento':data_nascimento,
                'gasto_total_par':gasto_total_par,
                'gasto_jan_par':gasto_jan_par,
                'gasto_fev_par':gasto_fev_par,
                'gasto_mar_par':gasto_mar_par,
                'gasto_abr_par':gasto_abr_par,
                'gasto_maio_par':gasto_maio_par,
                'gasto_junho_par':gasto_junho_par,
                'gasto_jul_par':gasto_jul_par,
                'gasto_agosto_par':gasto_agosto_par,
                'gasto_set_par':gasto_set_par,
                'gasto_out_par':gasto_out_par,
                'gasto_nov_par':gasto_nov_par,
                'gasto_dez_par':gasto_dez_par,
                'salario_bruto':salario_bruto_par_result,
                'gasto_total_gab':gasto_total_gab,
                'gasto_jan_gab':gasto_jan_gab,
                'gasto_fev_gab':gasto_fev_gab,
                'gasto_mar_gab':gasto_mar_gab,
                'gasto_abr_gab':gasto_abr_gab,
                'gasto_maio_gab':gasto_maio_gab,
                'gasto_junho_gab':gasto_junho_gab,
                'gasto_jul_gab':gasto_julho_gab,
                'gasto_agosto_gab':gasto_agosto_gab,
                'gasto_set_gab':gasto_set_gab,
                'gasto_out_gab':gasto_out_gab,
                'gasto_nov_gab':gasto_nov_gab,
                'gasto_dez_gab':gasto_dez_gab,
                'gasto_total_gab':gasto_total_gab,
        }
        
        # for i in dep:
        #     body = i
        #     dep_nome = Selector(text=body).xpath('//*[@id="nomedeputado"]').get()
        #     print(dep_nome)
        
        # # Salva o html da pagina
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')

        # # Salva os links em txt
        # file=open('lista_deputadas.txt','w')
        # for items in lista_deputadas:
        #     file.writelines(items+'\n')

        # file.close()