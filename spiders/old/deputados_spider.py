from wsgiref import headers
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "raspador_deputados"

    def start_requests(self):
        urls = [
"https://www.camara.leg.br/deputados/141431",
"https://www.camara.leg.br/deputados/92699",
"https://www.camara.leg.br/deputados/204427",
"https://www.camara.leg.br/deputados/204411",
"https://www.camara.leg.br/deputados/141434",
"https://www.camara.leg.br/deputados/191923",
"https://www.camara.leg.br/deputados/204392",
"https://www.camara.leg.br/deputados/204510",
"https://www.camara.leg.br/deputados/204494",
"https://www.camara.leg.br/deputados/204393",
"https://www.camara.leg.br/deputados/115746",
"https://www.camara.leg.br/deputados/160669",
"https://www.camara.leg.br/deputados/204473",
"https://www.camara.leg.br/deputados/204484",
"https://www.camara.leg.br/deputados/204527",
"https://www.camara.leg.br/deputados/204394",
"https://www.camara.leg.br/deputados/74383",
"https://www.camara.leg.br/deputados/204575",
"https://www.camara.leg.br/deputados/204491",
"https://www.camara.leg.br/deputados/74270",
"https://www.camara.leg.br/deputados/204365",
"https://www.camara.leg.br/deputados/160673",
"https://www.camara.leg.br/deputados/178996",
"https://www.camara.leg.br/deputados/74060",
"https://www.camara.leg.br/deputados/178916",
"https://www.camara.leg.br/deputados/204367",
"https://www.camara.leg.br/deputados/204454",
"https://www.camara.leg.br/deputados/204409",
"https://www.camara.leg.br/deputados/160528",
"https://www.camara.leg.br/deputados/62881",
"https://www.camara.leg.br/deputados/160552",
"https://www.camara.leg.br/deputados/116379",
"https://www.camara.leg.br/deputados/205548",
"https://www.camara.leg.br/deputados/204511",
"https://www.camara.leg.br/deputados/204451",
"https://www.camara.leg.br/deputados/178908",
"https://www.camara.leg.br/deputados/204512",
"https://www.camara.leg.br/deputados/204569",
"https://www.camara.leg.br/deputados/164359",
"https://www.camara.leg.br/deputados/204542",
"https://www.camara.leg.br/deputados/160588",
"https://www.camara.leg.br/deputados/178929",
"https://www.camara.leg.br/deputados/160599",
"https://www.camara.leg.br/deputados/143632",
"https://www.camara.leg.br/deputados/160758",
"https://www.camara.leg.br/deputados/204450",
"https://www.camara.leg.br/deputados/204518",
"https://www.camara.leg.br/deputados/204481",
"https://www.camara.leg.br/deputados/204439",
"https://www.camara.leg.br/deputados/204351",
"https://www.camara.leg.br/deputados/204412",
"https://www.camara.leg.br/deputados/204562",
"https://www.camara.leg.br/deputados/141417",
"https://www.camara.leg.br/deputados/74655",
"https://www.camara.leg.br/deputados/204541",
"https://www.camara.leg.br/deputados/92346",
"https://www.camara.leg.br/deputados/204500",
"https://www.camara.leg.br/deputados/178977",
"https://www.camara.leg.br/deputados/141421",
"https://www.camara.leg.br/deputados/141422",
"https://www.camara.leg.br/deputados/204364",
"https://www.camara.leg.br/deputados/160532",
"https://www.camara.leg.br/deputados/204389",
"https://www.camara.leg.br/deputados/178854",
"https://www.camara.leg.br/deputados/198783",
"https://www.camara.leg.br/deputados/161550",
"https://www.camara.leg.br/deputados/132504",
"https://www.camara.leg.br/deputados/204537",
"https://www.camara.leg.br/deputados/160640",
"https://www.camara.leg.br/deputados/204482",
"https://www.camara.leg.br/deputados/178871",
"https://www.camara.leg.br/deputados/178953",
"https://www.camara.leg.br/deputados/68720",
"https://www.camara.leg.br/deputados/178969",
"https://www.camara.leg.br/deputados/141427",
"https://www.camara.leg.br/deputados/171623",
"https://www.camara.leg.br/deputados/204368",
"https://www.camara.leg.br/deputados/160587",
"https://www.camara.leg.br/deputados/66828",
"https://www.camara.leg.br/deputados/204477",
"https://www.camara.leg.br/deputados/72442",
"https://www.camara.leg.br/deputados/204398",
"https://www.camara.leg.br/deputados/204371",
"https://www.camara.leg.br/deputados/160666",
"https://www.camara.leg.br/deputados/204426",
"https://www.camara.leg.br/deputados/141398",
"https://www.camara.leg.br/deputados/204499",
"https://www.camara.leg.br/deputados/204370",
"https://www.camara.leg.br/deputados/178876",
"https://www.camara.leg.br/deputados/204488",
"https://www.camara.leg.br/deputados/141405",
"https://www.camara.leg.br/deputados/73441",
"https://www.camara.leg.br/deputados/204496",
"https://www.camara.leg.br/deputados/204504",
"https://www.camara.leg.br/deputados/205476",
"https://www.camara.leg.br/deputados/204490",
"https://www.camara.leg.br/deputados/141439",
"https://www.camara.leg.br/deputados/204476",
"https://www.camara.leg.br/deputados/204440",
"https://www.camara.leg.br/deputados/74537",
"https://www.camara.leg.br/deputados/141408",
"https://www.camara.leg.br/deputados/204376",
"https://www.camara.leg.br/deputados/204378",
"https://www.camara.leg.br/deputados/204514",
"https://www.camara.leg.br/deputados/178963",
"https://www.camara.leg.br/deputados/135054",
"https://www.camara.leg.br/deputados/204355",
"https://www.camara.leg.br/deputados/141411",
"https://www.camara.leg.br/deputados/74467",
"https://www.camara.leg.br/deputados/152605",
"https://www.camara.leg.br/deputados/204419",
"https://www.camara.leg.br/deputados/74419",
"https://www.camara.leg.br/deputados/204513",
"https://www.camara.leg.br/deputados/160667",
"https://www.camara.leg.br/deputados/204442",
"https://www.camara.leg.br/deputados/73460",
"https://www.camara.leg.br/deputados/204408",
"https://www.camara.leg.br/deputados/204456",
"https://www.camara.leg.br/deputados/204465",
"https://www.camara.leg.br/deputados/204548",
"https://www.camara.leg.br/deputados/178964",
"https://www.camara.leg.br/deputados/178873",
"https://www.camara.leg.br/deputados/204373",
"https://www.camara.leg.br/deputados/178909",
"https://www.camara.leg.br/deputados/204444",
"https://www.camara.leg.br/deputados/73482",
"https://www.camara.leg.br/deputados/204539",
"https://www.camara.leg.br/deputados/178981",
"https://www.camara.leg.br/deputados/73772",
"https://www.camara.leg.br/deputados/178884",
"https://www.camara.leg.br/deputados/178959",
"https://www.camara.leg.br/deputados/141450",
"https://www.camara.leg.br/deputados/160674",
"https://www.camara.leg.br/deputados/109429",
"https://www.camara.leg.br/deputados/141335",
"https://www.camara.leg.br/deputados/204358",
"https://www.camara.leg.br/deputados/178948",
"https://www.camara.leg.br/deputados/204388",
"https://www.camara.leg.br/deputados/141513",
"https://www.camara.leg.br/deputados/204561",
"https://www.camara.leg.br/deputados/160538",
"https://www.camara.leg.br/deputados/74052",
"https://www.camara.leg.br/deputados/204551",
"https://www.camara.leg.br/deputados/204502",
"https://www.camara.leg.br/deputados/93083",
"https://www.camara.leg.br/deputados/204352",
"https://www.camara.leg.br/deputados/204572",
"https://www.camara.leg.br/deputados/178829",
"https://www.camara.leg.br/deputados/204531",
"https://www.camara.leg.br/deputados/178924",
"https://www.camara.leg.br/deputados/204487",
"https://www.camara.leg.br/deputados/141401",
"https://www.camara.leg.br/deputados/204361",
"https://www.camara.leg.br/deputados/178962",
"https://www.camara.leg.br/deputados/178993",
"https://www.camara.leg.br/deputados/204460",
"https://www.camara.leg.br/deputados/74262",
"https://www.camara.leg.br/deputados/141470",
"https://www.camara.leg.br/deputados/204386",
"https://www.camara.leg.br/deputados/204472",
"https://www.camara.leg.br/deputados/204391",
"https://www.camara.leg.br/deputados/160619",
"https://www.camara.leg.br/deputados/74079",
"https://www.camara.leg.br/deputados/204555",
"https://www.camara.leg.br/deputados/74554",
"https://www.camara.leg.br/deputados/209189",
"https://www.camara.leg.br/deputados/74141",
"https://www.camara.leg.br/deputados/204563",
"https://www.camara.leg.br/deputados/215043",
"https://www.camara.leg.br/deputados/204474",
"https://www.camara.leg.br/deputados/204420",
"https://www.camara.leg.br/deputados/74317",
"https://www.camara.leg.br/deputados/204372",
"https://www.camara.leg.br/deputados/73586",
"https://www.camara.leg.br/deputados/204457",
"https://www.camara.leg.br/deputados/204520",
"https://www.camara.leg.br/deputados/204497",
"https://www.camara.leg.br/deputados/204574",
"https://www.camara.leg.br/deputados/204550",
"https://www.camara.leg.br/deputados/178886",
"https://www.camara.leg.br/deputados/204536",
"https://www.camara.leg.br/deputados/151208",
"https://www.camara.leg.br/deputados/98057",
"https://www.camara.leg.br/deputados/178825",
"https://www.camara.leg.br/deputados/204359",
"https://www.camara.leg.br/deputados/204547",
"https://www.camara.leg.br/deputados/74156",
"https://www.camara.leg.br/deputados/74299",
"https://www.camara.leg.br/deputados/92102",
"https://www.camara.leg.br/deputados/74585",
"https://www.camara.leg.br/deputados/204382",
"https://www.camara.leg.br/deputados/196358",
"https://www.camara.leg.br/deputados/204523",
"https://www.camara.leg.br/deputados/204404",
"https://www.camara.leg.br/deputados/178879",
"https://www.camara.leg.br/deputados/74478",
"https://www.camara.leg.br/deputados/178931",
"https://www.camara.leg.br/deputados/178954",
"https://www.camara.leg.br/deputados/204381",
"https://www.camara.leg.br/deputados/160510",
"https://www.camara.leg.br/deputados/204448",
"https://www.camara.leg.br/deputados/160542",
"https://www.camara.leg.br/deputados/150418",
"https://www.camara.leg.br/deputados/204522",
"https://www.camara.leg.br/deputados/160535",
"https://www.camara.leg.br/deputados/204431",
"https://www.camara.leg.br/deputados/204506",
"https://www.camara.leg.br/deputados/74158",
"https://www.camara.leg.br/deputados/178858",
"https://www.camara.leg.br/deputados/204403",
"https://www.camara.leg.br/deputados/204566",
"https://www.camara.leg.br/deputados/178843",
"https://www.camara.leg.br/deputados/75431",
"https://www.camara.leg.br/deputados/204486",
"https://www.camara.leg.br/deputados/74749",
"https://www.camara.leg.br/deputados/141508",
"https://www.camara.leg.br/deputados/188097",
"https://www.camara.leg.br/deputados/178985",
"https://www.camara.leg.br/deputados/92172",
"https://www.camara.leg.br/deputados/154178",
"https://www.camara.leg.br/deputados/178895",
"https://www.camara.leg.br/deputados/204449",
"https://www.camara.leg.br/deputados/204415",
"https://www.camara.leg.br/deputados/146307",
"https://www.camara.leg.br/deputados/74165",
"https://www.camara.leg.br/deputados/178896",
"https://www.camara.leg.br/deputados/204384",
"https://www.camara.leg.br/deputados/204479",
"https://www.camara.leg.br/deputados/74352",
"https://www.camara.leg.br/deputados/178986",
"https://www.camara.leg.br/deputados/194260",
"https://www.camara.leg.br/deputados/74159",
"https://www.camara.leg.br/deputados/204498",
"https://www.camara.leg.br/deputados/74399",
"https://www.camara.leg.br/deputados/178987",
"https://www.camara.leg.br/deputados/204363",
"https://www.camara.leg.br/deputados/73463",
"https://www.camara.leg.br/deputados/73692",
"https://www.camara.leg.br/deputados/204422",
"https://www.camara.leg.br/deputados/204441",
"https://www.camara.leg.br/deputados/204475",
"https://www.camara.leg.br/deputados/204573",
"https://www.camara.leg.br/deputados/160645",
"https://www.camara.leg.br/deputados/204485",
"https://www.camara.leg.br/deputados/204455",
"https://www.camara.leg.br/deputados/162332",
"https://www.camara.leg.br/deputados/204526",
"https://www.camara.leg.br/deputados/204418",
"https://www.camara.leg.br/deputados/179587",
"https://www.camara.leg.br/deputados/156190",
"https://www.camara.leg.br/deputados/179000",
"https://www.camara.leg.br/deputados/146788",
"https://www.camara.leg.br/deputados/204433",
"https://www.camara.leg.br/deputados/76874",
"https://www.camara.leg.br/deputados/133810",
"https://www.camara.leg.br/deputados/204558",
"https://www.camara.leg.br/deputados/204556",
"https://www.camara.leg.br/deputados/178983",
"https://www.camara.leg.br/deputados/179001",
"https://www.camara.leg.br/deputados/81055",
"https://www.camara.leg.br/deputados/204452",
"https://www.camara.leg.br/deputados/215045",
"https://www.camara.leg.br/deputados/178912",
"https://www.camara.leg.br/deputados/122974",
"https://www.camara.leg.br/deputados/204395",
"https://www.camara.leg.br/deputados/122158",
"https://www.camara.leg.br/deputados/160604",
"https://www.camara.leg.br/deputados/178844",
"https://www.camara.leg.br/deputados/204406",
"https://www.camara.leg.br/deputados/204524",
"https://www.camara.leg.br/deputados/73486",
"https://www.camara.leg.br/deputados/204390",
"https://www.camara.leg.br/deputados/204383",
"https://www.camara.leg.br/deputados/204446",
"https://www.camara.leg.br/deputados/178951",
"https://www.camara.leg.br/deputados/204567",
"https://www.camara.leg.br/deputados/141523",
"https://www.camara.leg.br/deputados/74161",
"https://www.camara.leg.br/deputados/73801",
"https://www.camara.leg.br/deputados/73788",
"https://www.camara.leg.br/deputados/215042",
"https://www.camara.leg.br/deputados/204362",
"https://www.camara.leg.br/deputados/160655",
"https://www.camara.leg.br/deputados/160556",
"https://www.camara.leg.br/deputados/160642",
"https://www.camara.leg.br/deputados/204570",
"https://www.camara.leg.br/deputados/160601",
"https://www.camara.leg.br/deputados/204553",
"https://www.camara.leg.br/deputados/74160",
"https://www.camara.leg.br/deputados/171617",
"https://www.camara.leg.br/deputados/141518",
"https://www.camara.leg.br/deputados/141516",
"https://www.camara.leg.br/deputados/178860",
"https://www.camara.leg.br/deputados/204538",
"https://www.camara.leg.br/deputados/193726",
"https://www.camara.leg.br/deputados/160517",
"https://www.camara.leg.br/deputados/160558",
"https://www.camara.leg.br/deputados/204461",
"https://www.camara.leg.br/deputados/204492",
"https://www.camara.leg.br/deputados/74400",
"https://www.camara.leg.br/deputados/133968",
"https://www.camara.leg.br/deputados/141488",
"https://www.camara.leg.br/deputados/90201",
"https://www.camara.leg.br/deputados/213274",
"https://www.camara.leg.br/deputados/178920",
"https://www.camara.leg.br/deputados/204489",
"https://www.camara.leg.br/deputados/152610",
"https://www.camara.leg.br/deputados/160653",
"https://www.camara.leg.br/deputados/204530",
"https://www.camara.leg.br/deputados/204366",
"https://www.camara.leg.br/deputados/141531",
"https://www.camara.leg.br/deputados/74693",
"https://www.camara.leg.br/deputados/204480",
"https://www.camara.leg.br/deputados/160651",
"https://www.camara.leg.br/deputados/178861",
"https://www.camara.leg.br/deputados/122466",
"https://www.camara.leg.br/deputados/178935",
"https://www.camara.leg.br/deputados/73466",
"https://www.camara.leg.br/deputados/74371",
"https://www.camara.leg.br/deputados/178887",
"https://www.camara.leg.br/deputados/73604",
"https://www.camara.leg.br/deputados/160635",
"https://www.camara.leg.br/deputados/178990",
"https://www.camara.leg.br/deputados/204416",
"https://www.camara.leg.br/deputados/160621",
"https://www.camara.leg.br/deputados/74044",
"https://www.camara.leg.br/deputados/74439",
"https://www.camara.leg.br/deputados/178889",
"https://www.camara.leg.br/deputados/204559",
"https://www.camara.leg.br/deputados/160632",
"https://www.camara.leg.br/deputados/204517",
"https://www.camara.leg.br/deputados/160592",
"https://www.camara.leg.br/deputados/204387",
"https://www.camara.leg.br/deputados/178921",
"https://www.camara.leg.br/deputados/73808",
"https://www.camara.leg.br/deputados/178933",
"https://www.camara.leg.br/deputados/204438",
"https://www.camara.leg.br/deputados/204437",
"https://www.camara.leg.br/deputados/204557",
"https://www.camara.leg.br/deputados/74356",
"https://www.camara.leg.br/deputados/204425",
"https://www.camara.leg.br/deputados/178947",
"https://www.camara.leg.br/deputados/92776",
"https://www.camara.leg.br/deputados/177282",
"https://www.camara.leg.br/deputados/178922",
"https://www.camara.leg.br/deputados/143084",
"https://www.camara.leg.br/deputados/204519",
"https://www.camara.leg.br/deputados/160976",
"https://www.camara.leg.br/deputados/197438",
"https://www.camara.leg.br/deputados/178934",
"https://www.camara.leg.br/deputados/157130",
"https://www.camara.leg.br/deputados/178863",
"https://www.camara.leg.br/deputados/195866",
"https://www.camara.leg.br/deputados/160610",
"https://www.camara.leg.br/deputados/74376",
"https://www.camara.leg.br/deputados/141553",
"https://www.camara.leg.br/deputados/204505",
"https://www.camara.leg.br/deputados/204396",
"https://www.camara.leg.br/deputados/74283",
"https://www.camara.leg.br/deputados/137070",
"https://www.camara.leg.br/deputados/204483",
"https://www.camara.leg.br/deputados/141555",
"https://www.camara.leg.br/deputados/204478",
"https://www.camara.leg.br/deputados/204532",
"https://www.camara.leg.br/deputados/178992",
"https://www.camara.leg.br/deputados/160569",
"https://www.camara.leg.br/deputados/178952",
"https://www.camara.leg.br/deputados/160518",
"https://www.camara.leg.br/deputados/74043",

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
        
        ausencia_plenario = int(ausencia_plenario_nj)+int(ausencia_plenario_j)
        print("ausencia plenário: "+str(ausencia_plenario))
        
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
        
       
        ausencia_comissao = ausencia_comissao_nj + ausencia_comissao_j
        print("ausencia_comissao: "+ausencia_comissao)
        
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
        #gasto_jan_par
        
        gasto_jan_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[1]/td[2]/text()').get()
        gasto_jan_par = str(gasto_jan_par).strip()
        print("gasto jan par: "+gasto_jan_par)
        
        print("------------------------")
        #gasto_fev_par
        
        gasto_fev_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[2]/td[2]/text()').get()
        gasto_fev_par = str(gasto_fev_par).strip()
        print("gasto fev par: "+gasto_fev_par)
        
        print("------------------------")
        #gasto_mar_par
        
        gasto_mar_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[3]/td[2]/text()').get()
        gasto_mar_par = str(gasto_mar_par).strip()
        print("gasto mar par: "+gasto_mar_par)
        
        print("------------------------")
        #gasto_abr_par
        
        gasto_abr_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[4]/td[2]/text()').get()
        gasto_abr_par = str(gasto_abr_par).strip()
        print("gasto abr par: "+gasto_abr_par)
        
        print("------------------------")
        #gasto_maio_par
        
        gasto_maio_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[5]/td[2]/text()').get()
        gasto_maio_par = str(gasto_maio_par).strip()
        print("gasto maio par: "+gasto_maio_par)
        
        print("------------------------")
        #gasto_junho_par
        
        gasto_junho_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[6]/td[2]/text()').get()
        gasto_junho_par = str(gasto_junho_par).strip()
        print("gasto junho par: "+gasto_junho_par)
        
        print("------------------------")
        #gasto_jul_par
        
        gasto_jul_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[7]/td[2]/text()').get()
        gasto_jul_par = str(gasto_jul_par).strip()
        print("gasto jul par: "+gasto_jul_par)
        
        print("------------------------")
        #gasto_agosto_par
        
        gasto_agosto_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[8]/td[2]/text()').get()
        gasto_agosto_par = str(gasto_agosto_par).strip()
        print("gasto agosto par: "+gasto_agosto_par)
        
        print("------------------------")
        #gasto_set_par
        
        gasto_set_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[9]/td[2]/text()').get()
        gasto_set_par = str(gasto_set_par).strip()
        print("gasto set par: "+gasto_set_par)
        
        print("------------------------")
        #gasto_out_par
        
        gasto_out_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[10]/td[2]/text()').get()
        gasto_out_par = str(gasto_out_par).strip()
        print("gasto out par: "+gasto_out_par)
        
        print("------------------------")
        #gasto_nov_par
        
        gasto_nov_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[11]/td[2]/text()').get()
        gasto_nov_par = str(gasto_nov_par).strip()
        print("gasto novpar: "+gasto_nov_par)
        
        print("------------------------")
        #gasto_dez_par
        
        gasto_dez_par = response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr[12]/td[2]/text()').get()
        gasto_dez_par = str(gasto_dez_par).strip()
        print("gasto dez par: "+gasto_dez_par)
        
        print("------------------------")
        #salario_bruto_par
        #desconsiderar
  
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
        
        print("qtd viagem: "+quant_viagem)
        
        print("------------------------")
        
        yield {
                'nome': nome ,
                'sexo': "M",
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