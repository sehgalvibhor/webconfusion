function sidemenu(){
	document.getElementById('button-side-menu').style.display="none";
	document.getElementById('side-menu').style.display="block";
}
function closesidemenu(){
	document.getElementById('button-side-menu').style.display="block";
	document.getElementById('side-menu').style.display="none";
}
function run(){
 var html = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,
    styleActiveLine: true,
    matchBrackets: true,
  });
 var html=editor.CodeMirror.getValue();
 alert(html);
}