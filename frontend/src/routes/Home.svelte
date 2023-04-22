<script>
    import fastapi from "../lib/api"
    let question_list = []
    function get_question_list() {
        /*
        fetch("http://localhost:8000/api/question/list").then((response) => {
            response.json().then((json) => {
                question_list = json
            })
        })*/
        // ../lib/api.js 파일에 선언된 변수 fastapi = (operation, url, params, success_callback, failure_callback)
        // failure_callback은 입력하지 않음 (입력되지 않았을때 alert로 표시: fastapi의 if/else문 참고)
        fastapi('get', '/api/question/list', {}, (json) => {  // success_callback인 (jason)는 화살표 함수로 전달
            question_list = json
        })
    }
    get_question_list()
</script>

<ul>
    {#each question_list as question}
        <li>{question.subject}</li>
    {/each}
</ul>