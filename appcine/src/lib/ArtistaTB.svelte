<script>
    let promise = getArtista_by_name();

    async function getArtista_by_name() {
        const res = await fetch(
            `http://localhost:8000/artista/nome/Jennifer Aniston`
        );
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    function handleClick() {
        promise = getArtista_by_name();
    }
</script>

<!-- <button on:click={handleClick}> Listar artista </button>   -->

{#await promise}
    <p>Carrengando...</p>
{:then artista}
    <table class="border-collapse border border-slate-400">
        <thead>
            <tr>
                <th class="border border-slate-300">ID</th>
                <th class="border border-slate-300">Nome</th>
                <th class="border border-slate-300">Popularidade</th>
                <th class="border border-slate-300">Imagem</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="border border-slate-300">{artista["id"]}</td>
                <td class="border border-slate-300">{artista["nome"]}</td>
                <td class="border border-slate-300"
                    >{artista["popularidade"]}</td
                >
                <td class="border border-slate-300">
                    <img
                        src="https://image.tmdb.org/t/p/w185{artista['imagem']}"
                        alt="imagem do artista"
                        width="200"
                        height="200"
                    />
                </td></tr
            >
        </tbody>
    </table>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}

<!-- <style>
    .data {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
    }
</style> -->
