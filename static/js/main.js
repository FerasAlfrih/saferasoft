function toTitleCase(string){
	return string.charAt(0).toUpperCase() + string.slice(1);
}
function setActive() {
	
	var activePage = window.location.href;
	activePage=activePage.split("/", 20);
	activePage=activePage[activePage.length -2];
	console.log(activePage);
	activePage =toTitleCase(activePage);
	console.log(activePage);
	var btn = document.getElementById(activePage); 
	btn.className += ' active'; 

 	
};
window.onload=setActive();