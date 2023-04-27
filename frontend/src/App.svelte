<script>
  // svelte에서는 import를 먼저 하고 from을 쓴다.
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"

  const routes = {
    '/': Home,
    '/detail/:question_id': Detail,
  }
</script>

<Router {routes}/>