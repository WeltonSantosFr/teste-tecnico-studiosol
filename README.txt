crie seu ambiente virtual usando o comando python -m venv venv
rode o comando pip install -r requirements.txt para instalar todas as dependencias do projeto
então rode python manage.py runserver para rodar a aplicação localmente na porta 8000

a aplicação possui apenas uma rota localhost:8000/verify, onde recebe uma requisição POST em formato JSON contendo a senha, 
e as regras que a senha deve obedecer:

{
"password": "TesteSenhaForte!123&",
"rules": [
{"rule": "minSize","value": 8},
{"rule": "minSpecialChars","value": 2},
{"rule": "noRepeted","value": 0},
{"rule": "minDigit","value": 4}
]
},

e então retorna uma reposta tambem em formato JSON:

{
"verify": false,
"noMatch": ["minDigit"]
}

para enviar a requisição é indicado algum programa como insomnia ou postman :)