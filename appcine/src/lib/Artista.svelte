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

<!-- <button on:click={handleClick}> Listar artista </button> -->

{#await promise}
    <p>Carregando...</p>
{:then artista}
    <div class="table">
        <!-- {#each artista as a} -->
        <p>{artista["id"]}</p>
        <p>{artista["nome"]}</p>
        <!-- svelte-ignore a11y-missing-attribute -->
        <p><img src={artista["imagem"]} /></p>
        <p>{artista["popularidade"]}</p>
        <!-- TODO: salvar filme como favorito -->
        <!-- <p>Save</p> -->
        <!-- {/each} -->
    </div>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}

<style>
    .table {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr min-content;
        border: 1px solid #ccc;
        padding: 10px;
    }
</style>
