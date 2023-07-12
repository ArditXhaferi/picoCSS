<script>
    import Boxes from "../components/Boxes.svelte";
</script>

<main>
    <h1>Write style in seconds using <br> our Micro-CSS framework</h1>
    <span class="name"><svg fill="#6F47F7" aria-hidden="true" viewBox="0 0 418 42" preserveAspectRatio="none"><path d="M203.371.916c-26.013-2.078-76.686 1.963-124.73 9.946L67.3 12.749C35.421 18.062 18.2 21.766 6.004 25.934 1.244 27.561.828 27.778.874 28.61c.07 1.214.828 1.121 9.595-1.176 9.072-2.377 17.15-3.92 39.246-7.496C123.565 7.986 157.869 4.492 195.942 5.046c7.461.108 19.25 1.696 19.17 2.582-.107 1.183-7.874 4.31-25.75 10.366-21.992 7.45-35.43 12.534-36.701 13.884-2.173 2.308-.202 4.407 4.442 4.734 2.654.187 3.263.157 15.593-.78 35.401-2.686 57.944-3.488 88.365-3.143 46.327.526 75.721 2.23 130.788 7.584 19.787 1.924 20.814 1.98 24.557 1.332l.066-.011c1.201-.203 1.53-1.825.399-2.335-2.911-1.31-4.893-1.604-22.048-3.261-57.509-5.556-87.871-7.36-132.059-7.842-23.239-.254-33.617-.116-50.627.674-11.629.54-42.371 2.494-46.696 2.967-2.359.259 8.133-3.625 26.504-9.81 23.239-7.825 27.934-10.149 28.304-14.005.417-4.348-3.529-6-16.878-7.066Z"></path></svg>
        PicoCss
    </span>
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
    .example{
        display: flex;
        font-family: "sf-bold";
        z-index: 100000;
        max-width: 90rem;
        margin: 0 auto;
        height: 25rem;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .example div, .example img{

        position: relative;
        width: auto;
        height: 100%;
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
        src: url(sf-black.otf);
        font-weight: 900;
    }

    @font-face {
        font-family: sf-bold;
        src: url(sf-bold.otf);
        font-weight: 700;
    }

    @font-face {
        font-family: sf-regular;
        src: url(sf-regular.otf);
        font-weight: 400;
    }

    *{
        font-family: sf-regular;
    }

    h1{
        font-family: sf-black;
        color: #CCCCCC;
        font-size: 4rem;
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
        font-size: 6rem;
        text-align: center;
        color: #CCCCCC;
        -webkit-text-fill-color: transparent;
        -webkit-text-stroke: .3rem;
        position: relative;
        z-index: 100;
    }
    svg{
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
</style>