<script>
    import fastapi from "../lib/api"
    import {link} from 'svelte-spa-router'

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


<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr>
            <td>{i+1}</td>
            <td>
                <a use:link href="/detail/{question.id}">{question.subject}</a>
            </td>
            <td>{question.create_date}</td>
        </tr>
        {/each}
        </tbody>
    </table>
    <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>

<!-- 위의 테이블 표 코드를 작성하면서(부트스트랩) 일반 ul은 삭제 -->
<!-- <ul>
    {#each question_list as question}
        <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
</ul> -->