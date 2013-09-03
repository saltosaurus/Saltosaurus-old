function inputFocus(i){
    if(i.value==i.defaultValue){ i.value=""; i.style.color="#000"; }
}

function inputBlur(i){
    if(i.value==""){ i.value=i.defaultValue; i.style.color="#888"; }
}

function validateComment()
{
var x=document.forms["newComment"]["comment"].value;
if (x==null || x=="")
  {
  alert("You must write an actual comment before submitting.");
  return false;
  }
}