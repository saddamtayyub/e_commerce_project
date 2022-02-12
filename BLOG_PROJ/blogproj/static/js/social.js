

function commentToggle(parent_id){
    let row = document.getElementById(`comment_id`);
    if (row.classList.contains('d-none')){
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
    let btn = document.getElementById(`comment_btn`);
    console.log(btn.innerHTML)
    if (btn.innerHTML == "ADD NEW COMMENT"){
        btn.innerHTML = "CANCEL"
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-danger');
    } else{
        btn.innerHTML = "ADD NEW COMMENT"
        btn.classList.remove('btn-danger');
        btn.classList.add('btn-primary');
    }
}
console.log("hello there");

function commentReplyToggle(parent_id){
    let row = document.getElementById(`comment_${parent_id}`);
    if (row.classList.contains('d-none')){
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
    let btn = document.getElementById(`reply_btn`);
    console.log(btn.innerHTML)
    if (btn.innerHTML.includes("reply")){
        btn.innerHTML = "cancel"
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-danger');
    } else{
        btn.innerHTML = "reply"
        btn.classList.remove('btn-danger');
        btn.classList.add('btn-primary');
    }
}

function likeToggle(){
    let btn = document.getElementById(`like_btn`);
    if (btn.innerHTML.includes("LIKE")){
        btn.innerHTML = "DISLIKE"
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-danger');
    } else{
        btn.innerHTML = "LIKE"
        btn.classList.remove('btn-danger');
        btn.classList.add('btn-primary');
    }
}
