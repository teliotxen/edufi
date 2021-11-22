
 function ajaxPost(data){   
    //var data = { name: "1" }
    $.ajax({
        url: "", // 클라이언트가 HTTP 요청을 보낼 서버의 URL 주소
        data: JSON.stringify(data), // HTTP 요청과 함께 서버로 보낼 데이터// 문자열로 변환하여 저장
        method: "POST", // HTTP 요청 메소드(GET, POST 등)
        dataType: "json" // 서버에서 보내줄 데이터의 타입
    })
    .done(function(json) {
        var k = json
        console.log(typeof(k))
        console.log(JSON.parse(k))
    }) // HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달됨.
    .fail(function(xhr, status, errorThrown) {
        console.log('fail')
    })
    .always(function(xhr, status) {
        console.log('done')
    });
}
