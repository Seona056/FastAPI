<script>
  // svelte에서는 import를 먼저 하고 from을 쓴다.
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"

  const routes = {
    '/': Home,
  }
</script>

<Router {routes}/>