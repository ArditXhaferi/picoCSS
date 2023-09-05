<script>
import * as items from "./custom_data.json";

let filteredItems = items;

let searchTerm = "";

const searchItems = () => {	
    return filteredItems = Object.fromEntries(Object.entries(items).filter(([key, item]) => {
        let className = item.toString().toLowerCase();
        return className.includes(searchTerm.toLowerCase())
    }));
}

</script>

<div class="box">
    <label for="text">Search Any Utility Classes</label>
    <input placeholder="display: fl" type="text" bind:value={searchTerm} on:input={searchItems}>
    <div class="grid">
        {#each Object.entries(filteredItems) as [key, value]}
            <div class="item">
                <p>.{key} {'{'}</p>
                <span class="details">{@html value}</span>
            </div>
        {/each}
    </div>

</div>

<style>
    label{
        text-align: center;
        display: block;
        font-family: "sf-bold";
        margin: 0rem auto 1rem auto;
        width: fit-content;
        color: white;
        font-size: 2rem;
    }
    .box{
        margin-top: 5rem;
    }
    
    input{
        width: 12rem;
        height: 2rem;
        font-size: 2rem;
        font-family: "sf-bold";
        display: flex;
        margin: 0 auto;
        background-color: transparent;
        outline: 0;
        border: 2px solid white;
        border-radius: .2rem;
        padding: .4rem 1rem .4rem .6rem;
        color: #CCCCCC;
    }
    .grid{
        max-width: 70rem;
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        justify-content: center;
        gap: 1rem;
        margin-top: 5rem;
        margin-bottom: 10rem;
        overflow: hidden;
    }
    .item:hover .details{
        opacity: 1;
        transition: .3s ease;
    }
    .item:hover{
        height: 100%;
        max-height: 12rem;
        transition: .3s ease;
    }
    .details{
        opacity: 0;
        transition: .2s ease;
        overflow-y: scroll;
        max-width: 100%;
        max-height: 9rem;
        display: block;
    }
    p{
        font-size: 2rem;
        margin: 0;
    }
    .item{
        max-height: 3rem;
        transition: .4s ease;
        font-size: 1.4rem;
        border-radius: .4rem;
        width: 27%;
        height: 3rem;
        color: white;
        background-color: #17181C;
        border: 1px solid #CCCCCC;
        padding: .8rem 1.6rem;
    }
    @media only screen and (min-width: 768px) {
        .item{
            width: 19%;
        }
    }
    b{
        color: #6F47F7;
        font-family: sf-black;
    }
</style>
