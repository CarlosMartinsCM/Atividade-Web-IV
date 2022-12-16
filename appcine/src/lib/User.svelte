<script>

/** Função javascript*/

let resposta = "";
async function sendForm(e){
    let formData = new FormData(e.target);
    let data = Object.fromEntries(formData.entries());
    const res = await fetch('http://localhost:8000/user/create',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }); //Endpoint
    const json = await res.json();
    resposta = JSON.stringify(json);
}
</script>



<!--on:submit={create} Função javascript para o formulário-->
<h2>New user</h2>

<p>{resposta}</p>

<form class="crud" on:submit|preventDefault={sendForm}> <!--Formulário usuário-->
    <input type="text" name="name" placeholder="User name">
    <input type="text" name="email" placeholder="Email">
    <input type="text" name="password" placeholder="Password">

    <input type="submit" value="add"> <!-- Botão submit-->
</form>

<style>
    form.crud{
        display: grid;
        grid-template-columns: 1fr;
        gap: 5px;
    }
</style>