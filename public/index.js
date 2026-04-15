async function carregarAnimais(){
    const response = await axios.get("http://localhost:8000/animais/consulta/")

    const animais = response.data
    
    console.log(response.data)

    const lista = document.getElementById("lista-animais")

    const item = document.createElement("li")

    item.innerText = ""

    lista.innerHTML = ""

    animais.forEach(element => {
        const item  = document.createElement("li")

        const linha = `${element.nome} - idade: ${element.idade} - sexo ${element.sexo} - cor: ${element.cor}`

        item.innerText = linha
    
        lista.appendChild(item)
    });
}

function manipularAnimais(){

    const form_animal = document.getElementById("form_animal")
    const input_nome = document.getElementById('nome')

    form_animal.onsubmit = async (event)=>{
        event.preventDefault
        const nome_animal = input_nome.value
        alert(`submit chamado...${nome_animal}`)

        axios.post("http://localhost:8000/animais/", {
            nome: nome_animal,
            idade: 4, 
            sexo: 'macho',
            cor: 'branco'
        })

        alert("Animal cadastrado...")
    } 
}




function app(){
    console.log("App iniciado")
    carregarAnimais()
    manipularAnimais()
    carregarAnimais()
}

app()

