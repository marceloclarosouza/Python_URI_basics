# -*- coding: utf-8 -*-
"""
Testing chat bot. COVID19
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Test")

convI = ['Bom dia' , 'Bom dia', 'Boa tarde',  'Boa tarde', 'Boa noite', 'Boa noite', 'Tudo bem?', 'Tudo bem', 'oi', 'oi', 'tenho uma dúvida', 'Como possso te ajudar?']
convII = ['O que é covid-19?','É uma doença causada por um virus', 'O que é um virus?', 'É um organismo muito pequeno','ele foi feito pelos chineses?', 'não. é um virus silvestre natural']
convIII = ['Quais são os sintomas?', 'Febre, falta de ar, pneumonia', 'Pode afetar outros órgãos além dos pulmões?', 'Sim. POde afetar o coração, olhos e rins']
convIV = ['tem cura?', 'Sim, mas somente pelo próprio sistema imunológico', 'Tem vacina?', 'Ainda não', 'Pode matar', 'Sim, nos casos mais graves']
convV = ['Nós vamos morrer?', 'Infelizmente entre 5 e 10% da população morrerá', 'Posso pegar e não saber?', 'Sim, a maior parte dos casos são assintomáticos']
convVI = ['Quais países foram efetados?', 'Praticamente todos os países foram afetados pela pandemia', 'Os EUA vão salvar o mundo?', 'Não. Eles são os mais lascados']
convVII = ['Nosso governo está trbalhando direito?', 'Os governos estaudais sim. O Federal está deixando a desejar', 'Quantas pessoas foram infectadas?', 'No mundo tod 3,5 milhões. No Brasil 100 mil', 'Tem corona em ribeirão Preto?', 'Sim. temos 700 casos']

trainer = ListTrainer(bot)
trainer.train(convI)
trainer.train(convII)
trainer.train(convIII)
trainer.train(convIV)
trainer.train(convV)
trainer.train(convVI)
trainer.train(convVII)

while True:
  quest = input("Você: ")
  response = bot.get_response(quest)
  if float (response.confidence) > 0.5:
    print('FateBot: ', response)
  else:
    print("FateBot: Desculpe, não entendi, por favor refaça a pergunta.")

