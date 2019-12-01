function sendString(){
  var clicked = document.getElementById('input_string').value;
  $.ajax({
    type : "POST",
    url : "/sha",
    contentType: "application/json; charset=utf-8",
    data : JSON.stringify({'data': clicked}),
    dataType: "json",
    async: false,
    success: function(e){
      console.log("success");
      console.log(e['sha_value']);
      document.getElementById('sha_value').innerHTML = e['sha_value'];
    },error: function(e){
      console.log("error");
      console.log(e);
    }
  });
}


