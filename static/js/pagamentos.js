import pagarme from 'pagarme'

pagarme.client.connect({ api_key: 'chave' })
  .then(client => client.transactions.create({
    amount: 1000,
    card_number: '4111111111111111',
    card_holder_name: 'abc',
    card_expiration_date: '1225',
    card_cvv: '123',
  }))