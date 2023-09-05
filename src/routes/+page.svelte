<script>
    import Boxes from "../components/boxes.svelte";

    function copyFunction() {
        let text = "<link rel=\"stylesheet\" href=\"https://pico-css-succ.vercel.app/main.min.css\" />";
        navigator.clipboard.writeText(text);
        show();
    }

    let visible = false;

    function show() {
        visible = true;
        setTimeout(() => {
            visible = false;
        }, 3000); // Hide the alert after 3 seconds
    }

</script>

<main>
    <h1>Write style in seconds using <br> our Micro-CSS framework</h1>
    <span class="name"><svg class="svg" fill="#6F47F7" aria-hidden="true" viewBox="0 0 418 42" preserveAspectRatio="none"><path d="M203.371.916c-26.013-2.078-76.686 1.963-124.73 9.946L67.3 12.749C35.421 18.062 18.2 21.766 6.004 25.934 1.244 27.561.828 27.778.874 28.61c.07 1.214.828 1.121 9.595-1.176 9.072-2.377 17.15-3.92 39.246-7.496C123.565 7.986 157.869 4.492 195.942 5.046c7.461.108 19.25 1.696 19.17 2.582-.107 1.183-7.874 4.31-25.75 10.366-21.992 7.45-35.43 12.534-36.701 13.884-2.173 2.308-.202 4.407 4.442 4.734 2.654.187 3.263.157 15.593-.78 35.401-2.686 57.944-3.488 88.365-3.143 46.327.526 75.721 2.23 130.788 7.584 19.787 1.924 20.814 1.98 24.557 1.332l.066-.011c1.201-.203 1.53-1.825.399-2.335-2.911-1.31-4.893-1.604-22.048-3.261-57.509-5.556-87.871-7.36-132.059-7.842-23.239-.254-33.617-.116-50.627.674-11.629.54-42.371 2.494-46.696 2.967-2.359.259 8.133-3.625 26.504-9.81 23.239-7.825 27.934-10.149 28.304-14.005.417-4.348-3.529-6-16.878-7.066Z"></path></svg>
        PicoCss
    </span>
    {#if visible}
        <div class="alert-parent">
            <div class="alert">
                Stylesheet link is copied!
            </div>
        </div>
    {/if}
    <div class="github">
        <button on:click={copyFunction} class="link">
            <div class="copy"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" aria-hidden="true" class="icon"><path d="M278.9 511.5l-61-17.7c-6.4-1.8-10-8.5-8.2-14.9L346.2 8.7c1.8-6.4 8.5-10 14.9-8.2l61 17.7c6.4 1.8 10 8.5 8.2 14.9L293.8 503.3c-1.9 6.4-8.5 10.1-14.9 8.2zm-114-112.2l43.5-46.4c4.6-4.9 4.3-12.7-.8-17.2L117 256l90.6-79.7c5.1-4.5 5.5-12.3.8-17.2l-43.5-46.4c-4.5-4.8-12.1-5.1-17-.5L3.8 247.2c-5.1 4.7-5.1 12.8 0 17.5l144.1 135.1c4.9 4.6 12.5 4.4 17-.5zm327.2.6l144.1-135.1c5.1-4.7 5.1-12.8 0-17.5L492.1 112.1c-4.8-4.5-12.4-4.3-17 .5L431.6 159c-4.6 4.9-4.3 12.7.8 17.2L523 256l-90.6 79.7c-5.1 4.5-5.5 12.3-.8 17.2l43.5 46.4c4.5 4.9 12.1 5.1 17 .6z"></path></svg></div>
            https://pico-css-succ.vercel.app/main.min.css
        </button>
        <iframe src="https://ghbtns.com/github-btn.html?user=ArditXhaferi&repo=picoCSS&type=star&count=true&size=large" frameborder="0" scrolling="0" width="200" height="30" title="GitHub"></iframe>    </div>
    <div class="example">
        <div class="first">
            <img src="./first.png" alt="">
        </div>
        <div class="second">
            <img src="./second.png" alt="">
        </div>
    </div>

    <Boxes></Boxes>
</main>


<style>  

    iframe{
        margin-right: -100px;
    }
    .alert {
        position: absolute;
        bottom: 10px;
        right: 10px;
        background-color: #333;
        color: #fff;
        padding: 10px;
        border-radius: 5px;
        transition: opacity 0.3s;
        z-index: 1000000;
    }

    .hidden {
        opacity: 0;
        pointer-events: none;
    }
    .copy{
        display: flex;
    }

    button, input[type="submit"], input[type="reset"] {
        background: none;
        color: inherit;
        border: none;
        padding: 0;
        font: inherit;
        cursor: pointer;
        outline: inherit;
    }
    .link:hover{
        box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
        transform: translateY(-5px);
        transition: .3s ease;
    }
    .link{
        transition: .3s ease;
        outline: none;
        padding: 8px 16px;
        background-color: #6F47F7;
        border-radius: 8px;
        color: white;
        display: flex;
        align-items: center;
        gap: 1rem;
        cursor: pointer;
        overflow: hidden;
        max-width: 70%;
        white-space: nowrap;
    }

    .github{
        margin-top: 3rem;
        display: flex;
        justify-content: center;
        align-items: center; 
        flex-direction: column-reverse;
        gap: 2rem;
    }

    .github svg{
        width: 1.5rem;
        height: 1.5rem;
        fill: white;
    }
    .example{
        display: flex;
        font-family: "sf-bold";
        z-index: 100000;
        max-width: 90rem;
        margin: 0 auto;
        height: auto;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .example div, .example img{
        position: relative;
        width: 100%;
        height: auto;
    }
    .first::after{
        content: "tailwindcss";
        position: absolute;
        bottom: 1rem;
        left: 50%;
        font-size: 2rem;
        font-family: sf-black;
        color: white;
        background: #6F47F7;
        padding: .4rem 1rem;    
        border-radius: .2rem; 
        transform: translateX(-50%);   
    }
    .second::after{
        content: "PicoCSS";
        position: absolute;
        bottom: 1rem;
        left: 50%;
        font-size: 2rem;
        font-family: sf-black;
        color: white;
        background: #6F47F7;
        padding: .4rem 1rem;    
        border-radius: .2rem; 
        transform: translateX(-50%);   
    }
    @font-face {
        font-family: sf-black;
        src: url('/fonts/sf-black.otf');
        font-weight: 900;
    }

    @font-face {
        font-family: sf-bold;
        src: url('/fonts/sf-bold.otf');
        font-weight: 700;
    }

    @font-face {
        font-family: sf-regular;
        src: url('/fonts/sf-regular.otf');
        font-weight: 400;
    }

    *{
        font-family: sf-regular;
    }

    h1{
        font-family: sf-black;
        color: #CCCCCC;
        font-size: 2rem;
        text-align: center;
        margin-bottom: 1rem;
    }


    main{
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: flex-start;
        align-content: center;
        flex-direction: column;
    }
    .name{
        font-family: sf-black;
        font-size: 3.5rem;
        text-align: center;
        color: #CCCCCC;
        -webkit-text-fill-color: transparent;
        -webkit-text-stroke: .3rem;
        position: relative;
        z-index: 100;
    }
    .svg{
        z-index: -1;
        max-width: 25rem;
        position: absolute;
        bottom: -.5rem;
        left: 50%;
        transform: translateX(-50%);
    }
    main:before{
        background: radial-gradient(20% 50% at 50% 50%,rgb(111 71 247 / 38%) 0,rgba(37,38,44,0) 100%);
        content: "";
        position: absolute;
        inset: 0;
        z-index: 10;
        transform: scale(1);
        pointer-events: none;
    }

    @media only screen and (min-width: 768px) {
        h1{
            font-size: 4rem;
        }
        .name{
            font-size: 6rem;
        }
        .github{
            flex-direction: row;
        }
    }

    @media only screen and (min-width: 1324px) {
        .example{
            height: 25rem;
        }

        .example div, .example img{
            width: auto;
            height: 100%;
        }
    }
</style>